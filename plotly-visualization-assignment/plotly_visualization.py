import pandas as pd
import plotly.express as px

# Create dataset
epochs = list(range(1, 11))
loss = [0.9, 0.8, 0.7, 0.6, 0.55, 0.52, 0.50, 0.49, 0.48, 0.48]

# Create DataFrame using Pandas
df = pd.DataFrame({
    "Epoch": epochs,
    "Loss": loss
})

# Create interactive line chart
fig = px.line(
    df,
    x="Epoch",
    y="Loss",
    title="Training Loss Over Epochs",
    markers=True
)

# Add annotation where loss stabilizes
fig.add_annotation(
    x=8,
    y=0.49,
    text="Loss stabilizes here",
    showarrow=True,
    arrowhead=2
)

# Display chart
fig.show()
