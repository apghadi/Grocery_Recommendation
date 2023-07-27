import streamlit as st
import pickle
import numpy as np
import re

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )



with open('clustered_orders.p', 'rb') as file:
    clustered_orders = pickle.load(file)

with open('group_association_rules_dic.p', 'rb') as file:
    group_association_rules_dic = pickle.load(file)

with open('unique_products.p', 'rb') as file:
    unique_products = pickle.load(file)



def recommend(prod_name):
    prods=[]
    list_cluster = clustered_orders.loc[clustered_orders['product_name'] == prod_name, 'cluster'].unique()
    for i in list_cluster:
        if i <= 8:
            x = group_association_rules_dic[i]
            x = x[x["product_name_A"] == prod_name]
            if not x.empty:
                x= x.sort_values('lift', ascending = False)
                for j in range(0,min(3,len(x))):
                    if x.iloc[j]['product_name_B']:
                        prods.append(x.iloc[j]['product_name_B'])
    return prods


class Node:
	def __init__(self, newData):
		self.data = newData
		self.end = 0
		self.left = None
		self.eq = None
		self.right = None

def createNode(newData):
	newNode = Node(newData)
	newNode.end = 0
	newNode.left = None
	newNode.eq = None
	newNode.right = None
	return newNode


def insert(root, word, pos = 0):
	if not root:
		root = createNode(word[pos])
	if root.data > word[pos]:
		root.left = insert(root.left, word, pos)
	elif root.data < word[pos]:
		root.right = insert(root.right, word, pos)
	else:
		if pos + 1 == len(word):
			root.end = 1
		else:
			root.eq = insert(root.eq, word, pos + 1)
	return root
	


def traverse(root, ret, buff, depth = 0):
	if not root:
		return
	traverse(root.left, ret, buff, depth)
	buff[depth] = root.data
	if root.end:
		buff[depth + 1] = '\0'
		ret.append("".join(buff[:depth + 1]))
	traverse(root.eq, ret, buff, depth + 1)
	traverse(root.right, ret, buff, depth)


def util(root, pattern):
	buffer = [None] * 1001

	ret = []

	traverse(root, ret, buffer)

	if root.end == 1:
		ret.append(pattern)
	return ret


def autocomplete(root, pattern):
	words = []
	pos = 0
	if not pattern:
		return words
	while root and pos < len(pattern):
		if root.data > pattern[pos]:
			root = root.left
		elif root.data < pattern[pos]:
			root = root.right
			
		elif root.data == pattern[pos]:
			root = root.eq
			pos += 1
			
		else:
			return words
	
	words = util(root, pattern)
	
	return words


def print_suggestions(sugg, pat):
	for sug in sugg:
		print(pat + sug)



def show_predict_page():
    st.title("Grocery Recommendation System")
    st.write("""### We need some information to recommend similar products""")

    st.experimental_set_query_params(search='')
    query_params = st.experimental_get_query_params()
    search_query = query_params.get("search", "")
    search_query = st.text_input("Search", search_query)
    st.experimental_set_query_params(search=search_query)
    if search_query:
        regex = re.compile(f".*{search_query}.*", re.IGNORECASE)
        if regex:
            matches = [item for item in unique_products if regex.match(item)]
            if matches:
                selected_match = st.selectbox("Select an option", matches)
            else:
                selected_match = None
                st.write("No matches found.")	
        else:
            selected_match = None
            st.write("Invalid search query.")
    else:
        selected_match = None
	
    if selected_match in unique_products:
        item = selected_match
        ok = st.button("Add to cart")

        if ok:
            prods=recommend(item) 
            if prods:
                for i in prods:
                    st.subheader(i)
            else:
                st.write("Item added to cart!")
                st.write("Here are top products from our store")
                prods = ['Banana', 'Bag of Organic Bananas', 'Organic Strawberries', 'Organic Baby Spinach', 'Organic Hass Avocado']
                for i in prods:
                    st.subheader(i)

