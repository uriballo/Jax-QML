import plotly.express as px
import pandas as pd

# -------------------------
# First Year Tasks (Sept 2024 – Dec 2025)
# -------------------------
data_first_year = [
    # Literature Reviews
    dict(Task="Literature Reviews", Subtask="SoTA Review on Image encodings", Start="2024-09-01", Finish="2024-12-31"),
    dict(Task="Literature Reviews", Subtask="SoTA Review on Quantum Generative modelling", Start="2025-01-01", Finish="2025-04-30"),
    # Projects
    dict(Task="Projects", Subtask="ARQA Project", Start="2024-09-01", Finish="2025-06-30"),
    dict(Task="Publications", Subtask="ARQA Publication #1", Start="2025-02-01", Finish="2025-03-31"),
    dict(Task="Publications", Subtask="ARQA Publication #2", Start="2025-03-01", Finish="2025-06-30"),
    dict(Task="Projects", Subtask="Q-Care Project", Start="2025-04-01", Finish="2025-12-31"),
    dict(Task="Publications", Subtask="Q-Care Publication #1", Start="2025-09-01", Finish="2025-12-31"),
    dict(Task="Projects", Subtask="PRISMA Project", Start="2025-03-01", Finish="2025-12-31"),
    dict(Task="Literature Reviews", Subtask="PRISMA SoTA on Hyperparameter Optimization", Start="2025-03-01", Finish="2025-12-31"),

    dict(Task="Projects", Subtask="Testing models on Quantum Emulator and Real Hardware", Start="2025-09-01", Finish="2025-12-31"),
    # Implementations
    dict(Task="Implementations", Subtask="Quantum Diffusion Models 1st Approach", Start="2025-01-01", Finish="2025-03-31"),
    dict(Task="Implementations", Subtask="Quantum Circuit Models 1st Approach", Start="2025-03-01", Finish="2025-06-30"),
    dict(Task="Implementations", Subtask="Quantum GAN Models 1st Approach", Start="2025-03-01", Finish="2025-06-30")
]

df_first = pd.DataFrame(data_first_year)
df_first["Start"] = pd.to_datetime(df_first["Start"])
df_first["Finish"] = pd.to_datetime(df_first["Finish"])

fig1 = px.timeline(
    df_first,
    x_start="Start",
    x_end="Finish",
    y="Subtask",
    color="Task",
    title="PhD Plan - First Year",
    color_discrete_sequence=px.colors.qualitative.Plotly
)
fig1.update_yaxes(autorange="reversed")  # to list tasks from top to bottom
fig1.update_layout(
    xaxis_title="Timeline",
    yaxis_title="Subtasks",
    margin=dict(l=20, r=20, t=50, b=20),
    template="simple_white"
)
fig1.show()
# -------------------------
# Second Year Tasks (Jan 2026 – Dec 2026)
# -------------------------
data_second_year = [
    dict(Task="Publications", Subtask="Preparation of conference and journal submissions", Start="2026-01-01", Finish="2026-07-31"),
    dict(Task="Research", Subtask="Work on scaling of quantum generative models", Start="2026-01-01", Finish="2026-12-31"),
    dict(Task="Research", Subtask="Research Stay", Start="2026-09-01", Finish="2026-09-30")
]

df_second = pd.DataFrame(data_second_year)
df_second["Start"] = pd.to_datetime(df_second["Start"])
df_second["Finish"] = pd.to_datetime(df_second["Finish"])

fig2 = px.timeline(
    df_second,
    x_start="Start",
    x_end="Finish",
    y="Subtask",
    color="Task",
    title="PhD Plan - Second Year",
    color_discrete_sequence=px.colors.qualitative.Plotly
)
fig2.update_yaxes(autorange="reversed")
fig2.update_layout(
    xaxis_title="Timeline",
    yaxis_title="Subtasks",
    margin=dict(l=20, r=20, t=50, b=20),
    template="simple_white"
)
fig2.show()

# -------------------------
# Third Year Tasks (Jan 2027 – Sept 2027)
# -------------------------
data_third_year = [
    dict(Task="Thesis", Subtask="Thesis Writing", Start="2027-01-01", Finish="2027-09-30"),
    dict(Task="Publications", Subtask="Preparation of conference and journal submissions", Start="2027-01-01", Finish="2027-07-31")
]

df_third = pd.DataFrame(data_third_year)
df_third["Start"] = pd.to_datetime(df_third["Start"])
df_third["Finish"] = pd.to_datetime(df_third["Finish"])

fig3 = px.timeline(
    df_third,
    x_start="Start",
    x_end="Finish",
    y="Subtask",
    color="Task",
    title="PhD Plan - Third Year",
    color_discrete_sequence=px.colors.qualitative.Plotly
)
fig3.update_yaxes(autorange="reversed")
fig3.update_layout(
    xaxis_title="Timeline",
    yaxis_title="Subtasks",
    margin=dict(l=20, r=20, t=50, b=20),
    template="simple_white"
)
fig3.show()
