"""
Test Suite for Query Style Detection

Run with: python test_query_detection.py

Tests the simple heuristics against known semantic/keyword query examples
based on IR research and practical usage patterns.
"""

import sys
from typing import List, Tuple

# Import the detection functions
# (In actual integration, these would be from mlx_rerank.utils)
try:
    from query_detection_implementation import (
        detect_query_style,
        compute_semantic_score,
        QueryStyle,
    )
except ImportError:
    print("Error: Could not import query_detection_implementation module")
    print("Ensure query_detection_implementation.py is in the same directory")
    sys.exit(1)


# ============================================================================
# Test Data
# ============================================================================

SEMANTIC_QUERIES = [
    # Question word queries
    "what is machine learning",
    "how do I use asyncio in Python",
    "where can I find documentation",
    "when should I use async await",
    "why does my code hang",
    "who developed this framework",
    "which deployment method is best",

    # Question mark queries
    "how to deploy?",
    "what is asyncio?",
    "asyncio?",

    # Natural language / long queries
    "how to handle errors in asyncio applications",
    "best practices for asynchronous programming in Python",
    "what are the differences between sync and async",
    "can you explain how machine learning works",
    "would you recommend this for production use",

    # Dependency marker queries
    "how to deploy if load is high",
    "retry logic because network timeout",
    "error handling so that process continues",
    "deploy unless already deployed",

    # Paraphrased intent
    "I need to understand how async programming works",
    "tell me the pros and cons of this approach",
    "find me examples of good error handling",

    # Complex queries
    "what are the best practices for handling timeouts in asyncio when the network is slow",
    "how should I structure my code if I want to use async await but maintain backward compatibility",
]

KEYWORD_QUERIES = [
    # Short queries (1-3 words)
    "asyncio",
    "machine learning",
    "Python asyncio",
    "Kubernetes deployment",
    "Docker containers",

    # Proper nouns / entities
    "Amazon S3",
    "PostgreSQL monitoring",
    "Kubernetes Pods",
    "AWS Lambda",

    # Acronyms
    "API design",
    "HTTP requests",
    "REST endpoints",
    "JSON parsing",

    # Noun-phrase queries
    "best practices",
    "code optimization",
    "database performance",
    "web development frameworks",

    # Dense keyword packing (no stop words)
    "machine learning frameworks comparison",
    "Python async libraries",
    "database indexing strategies",
    "cloud deployment tools",

    # Entity lookup
    "Flask Django FastAPI",
    "Terraform Ansible Puppet",
    "React Vue Angular",

    # Product/tool names
    "pandas numpy scikit learn",
    "TensorFlow PyTorch",
    "Git GitHub GitLab",

    # Technical queries without question structure
    "error handling strategies",
    "code refactoring techniques",
    "performance optimization tips",
    "debugging best practices",
]

AMBIGUOUS_QUERIES = [
    # These could go either way depending on context
    ("how machine learning works", "SEMANTIC"),  # "how" is present
    ("machine learning how it works", "SEMANTIC"),  # Still has "how"
    ("Python how to deploy", "SEMANTIC"),  # "how" present
    ("deployment strategy", "KEYWORD"),  # No question structure
    ("async programming", "KEYWORD"),  # No question structure
    ("how to build", "SEMANTIC"),  # "how" present
    ("building systems", "KEYWORD"),  # No question structure
]


# ============================================================================
# Test Functions
# ============================================================================

def test_semantic_queries() -> Tuple[int, int]:
    """
    Test that all semantic queries are classified as SEMANTIC.

    Returns:
        (correct_count, total_count)
    """
    print("\n" + "=" * 70)
    print("Testing SEMANTIC Queries")
    print("=" * 70)

    correct = 0
    for query in SEMANTIC_QUERIES:
        result = detect_query_style(query)
        is_correct = result == QueryStyle.SEMANTIC
        correct += is_correct

        status = "✓" if is_correct else "✗"
        score = compute_semantic_score(query)

        print(f"{status} [{score:.2f}] {query}")

        if not is_correct:
            print(f"  ERROR: Expected SEMANTIC, got {result.value}")

    return correct, len(SEMANTIC_QUERIES)


def test_keyword_queries() -> Tuple[int, int]:
    """
    Test that all keyword queries are classified as KEYWORD.

    Returns:
        (correct_count, total_count)
    """
    print("\n" + "=" * 70)
    print("Testing KEYWORD Queries")
    print("=" * 70)

    correct = 0
    for query in KEYWORD_QUERIES:
        result = detect_query_style(query)
        is_correct = result == QueryStyle.KEYWORD
        correct += is_correct

        status = "✓" if is_correct else "✗"
        score = compute_semantic_score(query)

        print(f"{status} [{score:.2f}] {query}")

        if not is_correct:
            print(f"  ERROR: Expected KEYWORD, got {result.value}")

    return correct, len(KEYWORD_QUERIES)


def test_ambiguous_queries() -> Tuple[int, int]:
    """
    Test ambiguous queries that could go either way.

    Returns:
        (correct_count, total_count)
    """
    print("\n" + "=" * 70)
    print("Testing AMBIGUOUS Queries")
    print("=" * 70)

    correct = 0
    for query, expected_str in AMBIGUOUS_QUERIES:
        expected = QueryStyle.SEMANTIC if expected_str == "SEMANTIC" else QueryStyle.KEYWORD
        result = detect_query_style(query)
        is_correct = result == expected
        correct += is_correct

        status = "✓" if is_correct else "✗"
        score = compute_semantic_score(query)

        print(f"{status} [{score:.2f}] {query} → {result.value}")

        if not is_correct:
            print(f"  Expected {expected.value}, got {result.value}")

    return correct, len(AMBIGUOUS_QUERIES)


def test_edge_cases() -> Tuple[int, int]:
    """
    Test edge cases and boundary conditions.

    Returns:
        (correct_count, total_count)
    """
    print("\n" + "=" * 70)
    print("Testing EDGE CASES")
    print("=" * 70)

    test_cases = [
        ("", QueryStyle.KEYWORD),  # Empty query
        ("a", QueryStyle.KEYWORD),  # Single character
        ("?", QueryStyle.SEMANTIC),  # Just question mark
        ("what?", QueryStyle.SEMANTIC),  # Question word + mark
        ("What is this", QueryStyle.SEMANTIC),  # Capitalized question word
        ("WHAT IS THIS", QueryStyle.SEMANTIC),  # All caps
        ("...what do you mean", QueryStyle.SEMANTIC),  # With ellipsis
        ("how how how", QueryStyle.SEMANTIC),  # Repeated question word
        ("   how are you   ", QueryStyle.SEMANTIC),  # With whitespace
    ]

    correct = 0
    for query, expected in test_cases:
        result = detect_query_style(query)
        is_correct = result == expected
        correct += is_correct

        status = "✓" if is_correct else "✗"
        score = compute_semantic_score(query)

        display_query = f'"{query}"' if query else "(empty string)"
        print(f"{status} [{score:.2f}] {display_query} → {result.value}")

        if not is_correct:
            print(f"  Expected {expected.value}, got {result.value}")

    return correct, len(test_cases)


def test_score_ranges() -> None:
    """
    Test that semantic scores are in expected ranges.
    """
    print("\n" + "=" * 70)
    print("Testing SCORE RANGES")
    print("=" * 70)

    test_cases = [
        # Low scores (keyword-like)
        ("asyncio", 0.0, 0.3),
        ("machine learning", 0.0, 0.3),
        ("AWS S3", 0.0, 0.3),

        # Medium scores (ambiguous)
        ("how machine learning works", 0.4, 0.8),
        ("what is this framework", 0.4, 0.8),

        # High scores (semantic-like)
        ("what is machine learning?", 0.7, 1.0),
        ("how do I deploy this application", 0.7, 1.0),
        ("why does my code hang sometimes", 0.7, 1.0),
    ]

    for query, min_score, max_score in test_cases:
        score = compute_semantic_score(query)
        in_range = min_score <= score <= max_score

        status = "✓" if in_range else "✗"
        print(f"{status} {query}")
        print(f"  Score {score:.2f} in range [{min_score:.2f}, {max_score:.2f}]")

        if not in_range:
            print(f"  ERROR: Score out of expected range!")


# ============================================================================
# Main Test Runner
# ============================================================================

def main():
    print("\n" + "=" * 70)
    print("Query Style Detection - Comprehensive Test Suite")
    print("=" * 70)

    all_correct = 0
    all_total = 0

    # Test 1: Semantic queries
    correct, total = test_semantic_queries()
    all_correct += correct
    all_total += total
    semantic_accuracy = correct / total * 100 if total > 0 else 0
    print(f"\nSemantic Accuracy: {correct}/{total} ({semantic_accuracy:.1f}%)")

    # Test 2: Keyword queries
    correct, total = test_keyword_queries()
    all_correct += correct
    all_total += total
    keyword_accuracy = correct / total * 100 if total > 0 else 0
    print(f"\nKeyword Accuracy: {correct}/{total} ({keyword_accuracy:.1f}%)")

    # Test 3: Ambiguous queries
    correct, total = test_ambiguous_queries()
    all_correct += correct
    all_total += total
    ambiguous_accuracy = correct / total * 100 if total > 0 else 0
    print(f"\nAmbiguous Accuracy: {correct}/{total} ({ambiguous_accuracy:.1f}%)")

    # Test 4: Edge cases
    correct, total = test_edge_cases()
    all_correct += correct
    all_total += total
    edge_accuracy = correct / total * 100 if total > 0 else 0
    print(f"\nEdge Case Accuracy: {correct}/{total} ({edge_accuracy:.1f}%)")

    # Test 5: Score ranges
    test_score_ranges()

    # Summary
    print("\n" + "=" * 70)
    print("OVERALL RESULTS")
    print("=" * 70)
    overall_accuracy = all_correct / all_total * 100 if all_total > 0 else 0
    print(f"Total Accuracy: {all_correct}/{all_total} ({overall_accuracy:.1f}%)")

    # Success criteria
    if overall_accuracy >= 90:
        print("✓ PASS: Accuracy >= 90%")
        print("✓ Ready for production use")
        return 0
    elif overall_accuracy >= 80:
        print("⚠ MARGINAL: Accuracy 80-90%")
        print("✓ Acceptable for v1, consider improvements")
        return 0
    else:
        print("✗ FAIL: Accuracy < 80%")
        print("✗ Needs debugging")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
