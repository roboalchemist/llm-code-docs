proptest::bits
# Module i32 
Source 
## Constants§
ANYGenerates integers where all bits may be set.
## Functions§
betweenGenerates values where bits between the given bounds may be
set.maskedGenerates values where any bits set in `mask` (and no others)
may be set.sampledCreate a strategy which generates values where bits within the
bounds given by `bits` may be set. The number of bits that are
set is chosen to be in the range given by `size`.