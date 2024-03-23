import streamlit as st

def calculate_flames(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)
    
    combined_length = len(name1) + len(name2)
    result = ["Friend", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    
    while len(result) > 1:
        index = (combined_length % len(result)) - 1
        if index >= 0:
            right = result[index + 1 :]
            left = result[: index]
            result = right + left
        else:
            result = result[: len(result) - 1]
    
    return result[0]

def main():
    st.title("Flames Calculator")
    name1 = st.text_input("Enter Name 1:")
    name2 = st.text_input("Enter Name 2:")
    
    if st.button("Calculate"):
        if not name1 or not name2:
            st.warning("Please enter both names.")
        else:
            result = calculate_flames(name1, name2)
            st.success(f"Relationship status: {result}")

if __name__ == "__main__":
    main()
