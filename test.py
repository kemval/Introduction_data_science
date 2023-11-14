# Import necessary libraries
import plotly.express as px
import pandas as pd

# Create a sample dataset
data = {
    'Country': ['USA', 'Canada', 'UK', 'Germany', 'France'],
    'Population': [331002651, 37742154, 67886011, 83783942, 65273511],
    'GDP (Trillion $)': [21.43, 1.84, 2.83, 4.42, 2.78],
    'Happiness Index': [7.2, 7.6, 6.8, 6.9, 6.5]
}

df = pd.DataFrame(data)

# Create an interactive scatter plot using Plotly Express
fig = px.scatter(df, x='GDP (Trillion $)', y='Happiness Index', size='Population',
                 color='Country', hover_name='Country', log_x=True, size_max=60,
                 title='GDP vs Happiness Index with Population Size')

# Customize the layout
fig.update_layout(
    xaxis_title='GDP (Trillion $)',
    yaxis_title='Happiness Index',
    legend_title='Country',
)

# Show the plot
fig.show()


