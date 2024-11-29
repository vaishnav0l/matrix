import streamlit as st
import numpy as np

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

def main():
    st.title("Square Matrix Operations Calculator")

    st.sidebar.header("Choose Matrix Operations")

    # Input matrices and scalar
    matrix1_input = st.sidebar.text_area("Enter Matrix 1 (comma-separated values):")
    matrix2_input = st.sidebar.text_area("Enter Matrix 2 (comma-separated values):")
    scalar = st.sidebar.number_input("Enter Scalar Value:")

    try:
        # Convert input text to numpy arrays
        matrix1 = np.array([list(map(int, row.split(','))) for row in matrix1_input.split('\n') if row.strip()])
        matrix2 = np.array([list(map(int, row.split(','))) for row in matrix2_input.split('\n') if row.strip()])

        # Validate matrix dimensions for addition and subtraction
        if matrix1.shape != matrix2.shape:
            st.sidebar.error("Matrix 1 and Matrix 2 must have the same dimensions for addition and subtraction.")
            return
        
        # Validate dimensions for multiplication
        if matrix1.shape[1] != matrix2.shape[0]:
            st.sidebar.error("The number of columns in Matrix 1 must equal the number of rows in Matrix 2 for multiplication.")
            return

        if st.sidebar.button("Perform Operations"):
            # Perform operations and display results
            result_addition = add_matrices(matrix1, matrix2)
            result_subtraction = subtract_matrices(matrix1, matrix2)
            result_multiplication = multiply_matrices(matrix1, matrix2)
            result_scalar_multiply_for_1 = scalar_multiply(matrix1, scalar)
            result_scalar_multiply_for_2 = scalar_multiply(matrix2, scalar)
            result_transpose_for_1 = transpose_matrix(matrix1)
            result_transpose_for_2 = transpose_matrix(matrix2)

            st.subheader("Results:")

            # Display input matrices
            st.write("Matrix 1:")
            st.table(matrix1)

            st.write("Matrix 2:")
            st.table(matrix2)

            # Display results
            st.subheader("Matrix Addition:")
            st.table(result_addition)

            st.subheader("Matrix Subtraction:")
            st.table(result_subtraction)

            st.subheader("Matrix Multiplication:")
            st.table(result_multiplication)

            st.subheader(f"Scalar Multiplication with {scalar} for Matrix 1:")
            st.table(result_scalar_multiply_for_1)

            st.subheader(f"Scalar Multiplication with {scalar} for Matrix 2:")
            st.table(result_scalar_multiply_for_2)

            st.subheader("Transpose of Matrix 1:")
            st.table(result_transpose_for_1)

            st.subheader("Transpose of Matrix 2:")
            st.table(result_transpose_for_2)
    except ValueError:
        st.sidebar.error("Please ensure all matrix values are integers and properly formatted.")

if __name__ == "__main__"
 main()
