from preswald import text, plotly, connect, get_df, table,query
from preswald import slider
import pandas as pd
import plotly.express as px    

text("# Welcome to Preswald!")
text("This is your first app. 🎉")

# Load the CSV
connect() 
df = get_df('Mobiles_csv')  

sql = "SELECT * FROM Mobiles_csv WHERE RAM LIKE '12GB%'"
filtered_df = query(sql, "Mobiles_csv")

text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")

# Create a scatter plot
fig = px.scatter(df, x='Company Name', y='Launched Year', color='Launched Price (USA)',
                 title='Company Name vs. Launched Year',
                 labels={'company_name': 'Company Name', 'launched_year': 'Launched Year'})
# Style the plot
fig.update_layout(template='plotly_white')

# Show the plot
plotly(fig)

threshold = slider("Threshold", min_val=0, max_val=100, default=50)
table(df[df["Launched Year"] > threshold], title="Dynamic Data View")