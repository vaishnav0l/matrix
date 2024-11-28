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
    st.title("Matrix Operations Calculator")

    st.sidebar.header("Choose Matrix Operations")

    matrix1 = st.sidebar.text_area("Enter Matrix 1 (comma-separated values):")
    matrix2 = st.sidebar.text_area("Enter Matrix 2 (comma-separated values):")
    scalar = st.sidebar.number_input("Enter Scalar Value:")

    matrix1 = np.array([list(map(int, row.split(','))) for row in matrix1.split('\n') if row.strip()])
    matrix2 = np.array([list(map(int, row.split(','))) for row in matrix2.split('\n') if row.strip()])

    if st.sidebar.button("Perform Operations"):
        result_addition = add_matrices(matrix1, matrix2)
        result_subtraction = subtract_matrices(matrix1, matrix2)
        result_multiplication = multiply_matrices(matrix1, matrix2)
        result_scalar_multiply_for_1 = scalar_multiply(matrix1, scalar)
        result_scalar_multiply_for_2 = scalar_multiply(matrix2, scalar)
        result_transpose_for_1 = transpose_matrix(matrix1)
        result_transpose_for_2 = transpose_matrix(matrix2)

        st.subheader("Results:")

        # Display matrices using st.table for better formatting
        st.write("Matrix 1:")
        st.table(matrix1)

        st.write("Matrix 2:")
        st.table(matrix2)

        # Display results in a more organized way
        st.subheader("Matrix Addition:")
        st.table(result_addition)

        st.subheader("Matrix Subtraction:")
        st.table(result_subtraction)

        st.subheader("Matrix Multiplication:")
        st.table(result_multiplication)

        st.subheader(f"Scalar Multiplication with {scalar} For Matrix 1:")
        st.table(result_scalar_multiply_for_1)

        st.subheader(f"Scalar Multiplication with {scalar} For Matrix 2:")
        st.table(result_scalar_multiply_for_2)


        st.subheader("Transpose of Matrix 1:")
        st.table(result_transpose_for_1)

        st.subheader("Transpose of Matrix 2:")
        st.table(result_transpose_for_2)

if __name__ == "__main__":
    main()
