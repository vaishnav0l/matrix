import streamlit as st
import numpy as np

# Functions for matrix operations
def add_matrices(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def subtract_matrices(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)

def multiply_matrices(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

def scalar_multiply(matrix, scalar):
    return np.multiply(matrix, scalar)

def transpose_matrix(matrix):
    return np.transpose(matrix)

# Main Streamlit app function
def main():
    st.title("Enhanced Matrix Operations Calculator")
    st.sidebar.header("Choose Matrix Operations")

    # Matrix input areas with example defaults
    matrix1_input = st.sidebar.text_area("Enter Matrix 1 (comma-separated values, each row on a new line):",
                                         "1,2\n3,4")
    matrix2_input = st.sidebar.text_area("Enter Matrix 2 (optional, for operations requiring two matrices):",
                                         "5,6\n7,8")
    scalar = st.sidebar.number_input("Enter Scalar Value:", value=1)

    # Convert input text to numpy arrays with error handling
    try:
        matrix1 = np.array([list(map(int, row.split(','))) for row in matrix1_input.split('\n') if row.strip()])
        matrix2 = np.array([list(map(int, row.split(','))) for row in matrix2_input.split('\n') if row.strip()])
    except ValueError:
        st.error("Please enter valid integer values for the matrices.")
        return

    # Operation selection checkboxes
    operations = {
        "Addition": st.sidebar.checkbox("Addition", value=True),
        "Subtraction": st.sidebar.checkbox("Subtraction"),
        "Multiplication": st.sidebar.checkbox("Matrix Multiplication"),
        "Scalar Multiplication": st.sidebar.checkbox("Scalar Multiplication"),
        "Transpose": st.sidebar.checkbox("Transpose")
    }

    if st.sidebar.button("Perform Operations"):
        st.subheader("Input Matrices:")
        st.write("Matrix 1:")
        st.table(matrix1)

        if matrix2_input.strip():
            st.write("Matrix 2:")
            st.table(matrix2)

        st.subheader("Results:")

        # Perform selected operations
        if operations["Addition"]:
            if matrix1.shape == matrix2.shape:
                st.subheader("Matrix Addition:")
                st.table(add_matrices(matrix1, matrix2))
            else:
                st.error("Matrices must have the same shape for addition.")

        if operations["Subtraction"]:
            if matrix1.shape == matrix2.shape:
                st.subheader("Matrix Subtraction:")
                st.table(subtract_matrices(matrix1, matrix2))
            else:
                st.error("Matrices must have the same shape for subtraction.")

        if operations["Multiplication"]:
            if matrix1.shape[1] == matrix2.shape[0]:
                st.subheader("Matrix Multiplication:")
                st.table(multiply_matrices(matrix1, matrix2))
            else:
                st.error("Number of columns in Matrix 1 must match rows in Matrix 2 for multiplication.")

        if operations["Scalar Multiplication"]:
            st.subheader(f"Scalar Multiplication with {scalar}:")
            st.write("Matrix 1:")
            st.table(scalar_multiply(matrix1, scalar))
            if matrix2_input.strip():
                st.write("Matrix 2:")
                st.table(scalar_multiply(matrix2, scalar))

        if operations["Transpose"]:
            st.subheader("Transpose of Matrices:")
            st.write("Transpose of Matrix 1:")
            st.table(transpose_matrix(matrix1))
            if matrix2_input.strip():
                st.write("Transpose of Matrix 2:")
                st.table(transpose_matrix(matrix2))

if __name__ == "__main__":
    main()
