# %%writefile app.py%
import streamlit as st
# import pickle
import openpyxl
import xlrd
import numpy as np
import pandas as pd
# from sklearn.metrics.pairwise import cosine_similarity  
# from sklearn.metrics import pairwise_distances
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LinearRegression


# # loading the trained model
# tfidf_headline_features = pickle.load(open('PickleModel.pkl','rb'))


def main():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:#002E6D;padding:20px;font-weight:15px">
    <h1 style ="color:white;text-align:center;">Ephraim Adongo Customer Analytics</h1>
    </div>
    
    <div style ="background-color:#ADD8E6;">
    <h2 style ="color:black;text-align:center;"> This is a Soda Recommender system for Ephraim's Store</h2> 
    <h2 style ="color:black;text-align:center;"> It recommends the right type of soda to customers based on their Standard of living</h2>
    <h3 style ="color:black;text-align:center;"> Enter customer ID to get soda recommedation -- ID must be from 0 to 500 >>></h3>
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)
    default_value_goes_here = ""
    
    customer_id = int(st.number_input(''))
    
    
    global dataframe
#     if uploaded_file:
    df = pd.read_excel('output.xlsx')
    data_kmeans = df

    result = ""
    
    if st.button("Recommend"):
      soda_list = {'COKE':100, 'FANTA':60, 'SPRITE':40}
      def soda_recommenders(customer_id):
          id = int(customer_id)
          clus = int(data_kmeans.iloc[id,8])
          if clus == 0:
            st.write('The customer falls under the cluster WELL OFF\n')
            for key, value in soda_list.items():
              if value == 100:
                st.write('Soda Recommended for this customer is:\n')
                st.write(str(key)+'\nPrice: '+str(value))
          elif clus == 1:
            st.write('The customer falls under the cluster GOOD LIVING\n')
            for key, value in soda_list.items():
              if value == 60:
                st.write('Soda Recommended for this customer is:\n')
                st.write(str(key)+'\nPrice: '+str(value))
          else:
            st.write('The customer falls under the cluster STANDARD LIVING\n')
            for key, value in soda_list.items():
              if value == 40:
                st.write('Soda Recommended for this customer is:\n')
                st.write(str(key)+'\nPrice: '+str(value))
      result = soda_recommenders(customer_id)
#       for key, value in soda_list.items():
#             if value == 100 and result == 100:
#                 st.write('The customer falls under the cluster WELL OFF\n')
#                 st.write('Soda Recommended for this customer is:\n')
#                 if value == 100:
#                     st.write(str(key)+'\nPrice: '+str(value))
#             elif value == 60 and result == 60:
#                 st.write('The customer falls under the cluster GOOD LIVING\n')
#                 st.write('Soda Recommended for this customer is:\n')
#                 if value == 100:
#                     st.write(str(key)+'\nPrice: '+str(value))
#             else:
#                 st.write('The customer falls under the cluster STANDARD LIVING\n')
#                 st.write('Soda Recommended for this customer is:\n')
                
#                 st.write(str(key)+'\nPrice: '+str(value))
      st.write(result)
if __name__ == '__main__':
    main()
