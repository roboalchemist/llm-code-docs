# Create a fragment across multiple containers

Streamlit lets you turn functions into [fragments](https://docs.streamlit.io/develop/concepts/architecture/fragments), which can rerun independently from the full script. If your fragment doesn't write to outside containers, Streamlit will clear and redraw all the fragment elements with each fragment rerun. However, if your fragment _does_ write elements to outside containers, Streamlit will not clear those elements during a fragment rerun. Instead, those elements accumulate with each fragment rerun until the next full-script rerun. If you want a fragment to update multiple containers in your app, use `st.empty()` containers to prevent accumulating elements.

## Initialize your app

1. In `your_repository`, create a file named `app.py`.
2. In a terminal, change directories to `your_repository`, and start your app:

   ```bash
   streamlit run app.py
   ```

   Your app will be blank because you still need to add code.

3. In `app.py`, write the following:

   ```python
   import streamlit as st
   import time

   st.title("Cats!")

   row1 = st.columns(3)
   row2 = st.columns(3)

   grid = [col.container(height=200) for col in row1 + row2]
   safe_grid = [card.empty() for card in grid]

   def black_cats():
       time.sleep(1)
       st.title("🐈‍⬛ 🐈‍⬛")
       st.markdown("🐾 🐾 🐾 🐾")

   def orange_cats():
       time.sleep(1)
       st.title("🐈 🐈")
       st.markdown("🐾 🐾 🐾 🐾")

   @st.fragment
   def herd_black_cats(card_a, card_b, card_c):
       st.button("Herd the black cats")
       container_a = card_a.container()
       container_b = card_b.container()
       with container_a:
           black_cats()
       with container_b:
           black_cats()
       with container_c:
           black_cats()

   @st.fragment
   def herd_orange_cats(card_a, card_b, card_c):
       st.button("Herd the orange cats")
       container_a = card_a.container()
       container_b = card_b.container()
       container_c = card_c.container()
       with container_a:
           orange_cats()
       with container_b:
           orange_cats()
       with container_c:
           orange_cats()

   with st.sidebar:
       herd_black_cats(grid[0].empty(), grid[2].empty(), grid[4].empty())
       herd_orange_cats(grid[1].empty(), grid[3].empty(), grid[5].empty())
       st.button("Herd all the cats")
   ```

## Frame out your app's containers

1. Add a title to your app and two rows of three containers.

   ```python
   st.title("Cats!")

   row1 = st.columns(3)
   row2 = st.columns(3)

   grid = [col.container(height=200) for col in row1 + row2]
   ```

   Save your file to see your updated preview.

2. Define a helper function to draw two black cats.

   ```python
   def black_cats():
       time.sleep(1)
       st.title("🐈‍⬛ 🐈‍⬛")
       st.markdown("🐾 🐾 🐾 🐾")
   ```

   This function represents "herding two cats" and uses `time.sleep()` to simulate a slower process. You will use this to draw two cats in one of your grid cards later on.

3. Define another helper function to draw two orange cats.

   ```python
   def orange_cats():
       time.sleep(1)
       st.title("🐈 🐈")
       st.markdown("🐾 🐾 🐾 🐾")
   ```

4. Optional: Test out your functions by calling each one within a grid card.

   ```python
   with grid[0]:
       black_cats()
   with grid[1]:
       orange_cats()
   ```

   Save your `app.py` file to see the preview. Delete these four lines when finished.

## Define your fragments

Since each fragment will span across the sidebar and three additional containers, you'll use the sidebar to hold the main body of the fragment and pass the three containers as function arguments.

1. Use an `@st.fragment` decorator and start your black-cat fragment definition.

   ```python
   @st.fragment
   def herd_black_cats(card_a, card_b, card_c):
       st.button("Herd the black cats")
       container_a = card_a.container()
       container_b = card_b.container()
       container_c = card_c.container()
       with container_a:
           black_cats()
       with container_b:
           black_cats()
       with container_c:
           black_cats()
   ```

2. Add a button for rerunning this fragment.

   ```python
   st.button("Herd the black cats")
   ```

3. Write to each container using your helper function.

   ```python
   with card_a:
       black_cats()
   with card_b:
       black_cats()
   with card_c:
       black_cats()
   ```

   This code above will not behave as desired, but you'll explore and correct this in the following steps.

4. Test out your code. Call your fragment function in the sidebar.

   ```python
   with st.sidebar:
       herd_black_cats(grid[0].empty(), grid[2].empty(), grid[4].empty())
       herd_orange_cats(grid[1].empty(), grid[3].empty(), grid[5].empty())
       st.button("Herd all the cats")
   ```

   By creating `st.empty()` containers in each card and passing them to your fragments, you prevent elements from accumulating in the cards with each fragment rerun. If you create the `st.empty()` containers earlier in your app, full-script reruns will clear the orange-cat cards while (first) rendering the black-cat cards.

5. Include a button outside of your fragments. When clicked, the button will trigger a full-script rerun since you're calling its widget function outside of any fragment.

   ```python
   st.button("Herd all the cats")
   ```

6. Save your file and try out the app! When you click "Herd the black cats" or "Herd the orange cats", Streamlit will only redraw the three related cards. When you click "Herd all the cats", Streamlit redraws all six cards.