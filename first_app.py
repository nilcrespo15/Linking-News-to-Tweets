import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('Linking News to Tweets')


df = pd.read_csv("50_tweets.csv")


chart_data = pd.DataFrame(df,
     columns=['visibility','final_relevance'])

chart_data.columns = ['Visibility', 'Relevance']


if st.sidebar.checkbox('Show dataframe'):
    df

st.bar_chart(chart_data)

option = st.sidebar.selectbox(
    'What interests you more? Relevance or Visibility?',
     chart_data.columns)

'You selected:', option


expander = st.beta_expander("How many tweets do you want to visualize?")
expander.write("The best one")
expander.write("The two best ones")
expander.write("The top 3 tweets")


left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press to see the best tweet!')
if pressed:
    if option == 'Relevance':
	    right_column.image('tweet_rel.png', width=450)
	    left_column.write('Visibility rank')
	    left_column.write(chart_data.Visibility.loc[chart_data.Relevance == chart_data.Relevance.max()])
	    left_column.write('Relevance rank')
	    left_column.write(chart_data.Relevance.loc[chart_data.Relevance == chart_data.Relevance.max()])
    elif option == 'Visibility':
	    right_column.image('tweet_vis.png')
	    left_column.write('Visibility rank')
	    left_column.write(chart_data.Visibility.loc[chart_data.Visibility == chart_data.Visibility.max()])
	    left_column.write('Relevance rank')
	    left_column.write(chart_data.Relevance.loc[chart_data.Visibility == chart_data.Visibility.max()])




'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'


