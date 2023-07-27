import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def show_explore_page():
    st.title("Exploratory Data Analysis")

    image1 = Image.open("eda1.png")
    st.image(image1, caption="Products per Department")
    st.write("The bar graph in Figure 1 shows that 'Personal Care', 'Snacks', and 'Pantry' are the departments that offer the highest number of products, ’Personal Care’ being the highest in the ranking offering 6563 distinct products. The meat and Seafood section offers the least product. There are 1258 products that are not tagged to any department.")

    image2 = Image.open("eda2.png")
    st.image(image2, caption="Products per Aisle")
    st.write("The Bar graph in this figure shows the total number of products that each aisle offers. The top in this list is the missing products followed by Candy Chocolate offering a large variety of products.")
    
    image3 = Image.open("eda3.png")
    st.image(image3, caption="Max number of Products brought per Order")
    st.write("This figure shows that the maximum number of people buy 5-6 products in a single order and it gradually decreases after this value.")

    image4 = Image.open("eda4.png")
    st.image(image4, width=600, caption="Order Frequency")
    st.write("The data frame 'order products prior new' provides information about each order and the product with their Aisle id and department id associated with those orders. Using this data we have calculated the frequency of each item being purchased to identify the most popular items. Figure 4 shows the visualization for the same. This shows us that banana is the most bought product.")

    image5 = Image.open("eda5.png")
    st.image(image5, width=600, caption="Reorder Ratio")
    st.write("This figure shows the products which have the lowest rate of reorder. This includes 'Personal Care' and 'Pantry' products. The customer reviews can be used to dig deeper for identifying the low rate of reorder also such products need to be promoted more often to improve this ratio.")

    image6 = Image.open("eda6.png")
    st.image(image6, width=600, caption="Number of Orders taken during each Hour")
    st.write("This figure shows the busiest hours of the day during which the highest number of orders are placed. Between hours 10-16 of the day maximum number of orders are placed.")

    image7 = Image.open("eda7.png")
    st.image(image7, width=600, caption="Number of Orders taken on each Day of the Week")
    st.write("This figure shows the days on which the maximum number of orders are placed. The Maximum orders are taken on Monday or Tuesday and gradually decrease as the week progresses.")

    image8 = Image.open("eda8.png")
    st.image(image8, width=600, caption="Days Since Prior Order")
    st.write("This figure shows that people often re-order within a week. After a week period, the rate of reordering goes on decreasing grad- ually, and then after the period of 29 days, an unusual peak on the 30th day can be observed showing infrequent buyers reordering after 30 or more days.")

    image9 = Image.open("eda9.png")
    st.image(image9, width=600, caption="Order Rate on each Hour of each Day of the Week")
    st.write("Order Rate on each Hour of each Day of the Week Figure 9 shows that in the afternoon period i.e. between 10 AM and 4 PM on Monday and the Morning period i.e. between 9 AM and 11 AM on Tuesday the most traffic the customers can be seen. This window can be utilized for most of the promotions.")

    image10 = Image.open("eda10.png")
    st.image(image10, width=600, caption="Order Rate for each Aisle")
    st.write("This figure shows that the maximum number of products are ordered from the fresh fruit and fresh vegetables section.")

    image11 = Image.open("eda11.png")
    st.image(image11, width=600, caption="Order Rate for each Department")
    st.write(" This figure shows that the maximum number of products are ordered from the produce department.")

    image13 = Image.open("eda13.png")
    st.image(image13, width=600, caption="Elbow plot to determine optimal number of clusters")
    st.write(" This figure shows that 7 clusters will provide optimal results.")


    image12 = Image.open("eda12.png")
    st.image(image12, width=600, caption="Cluster Centroids")
    st.write(" This figure shows the centroids for all the 7 clusters.")





