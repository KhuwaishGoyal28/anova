import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from shiny import App, render, ui

# Load your dataset
df = pd.read_csv("hr_data.csv")  # Change this to your actual file

# Convert necessary columns to numeric
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['YearsAtCompany'] = pd.to_numeric(df['YearsAtCompany'], errors='coerce')

# Define UI
app_ui = ui.page_fluid(
    ui.h2("HR Analytics Dashboard", class_="text-center text-white bg-dark p-3"),

    # Top Metrics
    ui.layout_columns(
        ui.card(ui.h5("Total Employees"), ui.h3(str(len(df))), class_="card text-white bg-primary p-3"),
        ui.card(ui.h5("Attrition"), ui.h3(str(df['Attrition'].sum().item())), class_="card text-white bg-danger p-3"),
        ui.card(ui.h5("Attrition Rate"), ui.h3(f"{(df['Attrition'].sum() / df.shape[0]) * 100:.1f}%"), class_="card text-white bg-warning p-3"),
        ui.card(ui.h5("Average Age"), ui.h3(str(int(df['Age'].mean()))), class_="card text-white bg-success p-3"),
        ui.card(ui.h5("Average Salary"), ui.h3(f"{df['MonthlyIncome'].mean() / 1000:.1f}K"), class_="card text-white bg-info p-3"),
        ui.card(ui.h5("Average Years at Company"), ui.h3(str(int(df['YearsAtCompany'].mean()))), class_="card text-white bg-secondary p-3")
    ),

    # Dropdown Filter
    ui.input_selectize("department_filter", "Select Department(s):", 
                       choices=list(df['Department'].unique()), multiple=True),

    # Graphs
    ui.layout_columns(
        ui.output_plot("attrition_education"),
        ui.output_plot("attrition_age"),
        ui.output_plot("attrition_gender"),
        ui.output_plot("attrition_salary"),
        ui.output_plot("attrition_years"),
        ui.output_plot("attrition_jobrole")
    )
)

# Define Server Logic
def server(input, output, session):
    @output
    @render.plot
    def attrition_education():
        plt.figure(figsize=(8, 5))
        sns.countplot(x="Education", hue="Attrition", data=df, palette="coolwarm")
        plt.title("Attrition by Education Level")
        return plt.gca()

    @output
    @render.plot
    def attrition_age():
        plt.figure(figsize=(8, 5))
        sns.histplot(df[df['Attrition'] == 1]['Age'], bins=20, color="red", label="Attrition")
        sns.histplot(df[df['Attrition'] == 0]['Age'], bins=20, color="blue", label="No Attrition")
        plt.legend()
        plt.title("Age Distribution of Attrition")
        return plt.gca()

    @output
    @render.plot
    def attrition_gender():
        plt.figure(figsize=(6, 4))
        sns.countplot(x="Gender", hue="Attrition", data=df, palette="coolwarm")
        plt.title("Attrition by Gender")
        return plt.gca()

    @output
    @render.plot
    def attrition_salary():
        plt.figure(figsize=(8, 5))
        sns.boxplot(x="Attrition", y="MonthlyIncome", data=df, palette="coolwarm")
        plt.title("Salary vs Attrition")
        return plt.gca()

    @output
    @render.plot
    def attrition_years():
        plt.figure(figsize=(8, 5))
        sns.boxplot(x="Attrition", y="YearsAtCompany", data=df, palette="coolwarm")
        plt.title("Years at Company vs Attrition")
        return plt.gca()

    @output
    @render.plot
    def attrition_jobrole():
        plt.figure(figsize=(10, 5))
        sns.countplot(y="JobRole", hue="Attrition", data=df, palette="coolwarm")
        plt.title("Attrition by Job Role")
        return plt.gca()

# Run App on Port 8501
app = App(app_ui, server)
app.run(port=8501)
