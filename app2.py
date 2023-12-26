import calendar  # Core Python Module
from datetime import datetime  # Core Python Module

import plotly.graph_objects as go  # pip install plotly
import streamlit as st  # pip install streamlit
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu



# -------------- SETTINGS --------------
personal = ["Height (m)", "Weight (kg)", "Age"]
diets = ["Salt intake", "Fibre intake", "Caffeine intake"]
page_title = "H1ydration Tracker"
page_icon = ":potable_water:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# --- DROP DOWN VALUES FOR SELECTING THE PERIOD ---
#years = [datetime.today().year, datetime.today().year + 1]
#months = list(calendar.month_name[1:])


# --- DATABASE INTERFACE ---
def get_all_periods():
    items = db.fetch_all_periods()
    periods = [item["key"] for item in items]
    return periods


# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- NAVIGATION MENU ---
selected = option_menu(
    menu_title=None,
    options=["Data Entry", "Data Visualization"],
    icons=["pencil-fill", "bar-chart-fill"],  # https://icons.getbootstrap.com/
    orientation="horizontal",
)

# --- INPUT & SAVE PERIODS ---
if selected == "Data Entry":
    st.header(f"Data Entry")
    with st.form("entry_form", clear_on_submit=True):
        #col1 = st.columns(1)
        #col1.selectbox("Select Month:", months, key="month")

        "---"
        with st.expander("Personal Specifications"):
            for i in personal:
                st.number_input(f"{i}:", min_value=0, format="%i", step=1, key=personal)
        with st.expander("Diet (in grams)"):
            for diet in diets:
                st.number_input(f"{diet}:", min_value=0, format="%i", step=10, key=diets)

        "---"
        submitted = st.form_submit_button()
        if submitted:
            #period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
            personal = {Personals: st.session_state[i] for i in personal}
            diets = {expense: st.session_state[diet] for diet in diets}
            db.insert_period(period, personal, diets)
            st.success("Data saved!")


# --- PLOT PERIODS ---
if selected == "Data Visualization":
    st.header("Under construction")
    #with st.form("saved_periods"):
     #   period = st.selectbox("Select Period:", get_all_periods())
      #  submitted = st.form_submit_button("Plot Period")
       # if submitted:
        #    # Get data from database
         #   period_data = db.get_period(period)
          #  comment = period_data.get("comment")
           # expenses = period_data.get("expenses")
            #incomes = period_data.get("incomes")
#
 #           # Create metrics
  #          total_income = sum(incomes.values())
   #         total_expense = sum(expenses.values())
    #        remaining_budget = total_income - total_expense
     #       col1, col2, col3 = st.columns(3)
      #      col1.metric("Total Income", f"{total_income}")
       #     col2.metric("Total Expense", f"{total_expense}")
        #    col3.metric("Remaining Budget", f"{remaining_budget}")
         #   st.text(f"Comment: {comment}")
#
 #           # Create sankey chart
  #          label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
   #         source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
    #        target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses.keys()]
     #       value = list(incomes.values()) + list(expenses.values())
#
 #           # Data to dict, dict to sankey
  #          link = dict(source=source, target=target, value=value)
   #         node = dict(label=label, pad=20, thickness=30, color="#E694FF")
    #        data = go.Sankey(link=link, node=node)
#
 #           # Plot it!
  #          fig = go.Figure(data)
   #         fig.update_layout(margin=dict(l=0, r=0, t=5, b=5))
    #        st.plotly_chart(fig, use_container_width=True)
