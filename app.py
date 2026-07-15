import streamlit as st
import joblib

classifier=joblib.load('model.pkl')


st.title("IRIS CLASSIFICATION APP")
st.write("used for iris classification")
sl=st.number_input(label="Enter sepal length")
sw=st.number_input(label="Enter sepal Width")
pl=st.number_input(label="Enter petal length")
pw=st.number_input(label="Enter petal width")


if st.button("Predict"):
    result=classifier.predict([[sl,sw,pl,pw]])
    st.success(result[0])
result = classifier.predict([[sl,sw,pl,pw]])
if result[0]==0:
    st.write("The flower is setosa")
elif result[0]==1:
    st.write("The flower is versicolor")
else:
    st.write("The flower is virginica")