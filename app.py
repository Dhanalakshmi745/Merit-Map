
import streamlit as st
import pandas as pd
import pickle
import plotly.express as px

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Merit Map",
    page_icon="🎓",
    layout="wide"
)

# ==================================================
# LOAD DATA
# ==================================================

@st.cache_data
def load_data():
    return pd.read_csv("enhanced_college_dataset.csv")

df = load_data()

# Create Recommendation Score if missing

if "Recommendation_Score" not in df.columns:

    df["Seat_Ratio"] = (
        df["Available_Seats"] /
        df["Total_Seats"]
    )

    df["Recommendation_Score"] = (

        (100 - df["NIRF_Rank"]) * 0.30 +

        df["Placement_Percentage"] * 0.30 +

        df["Average_Package"] * 5 * 0.20 +

        df["Seat_Ratio"] * 100 * 0.20
    )

# ==================================================
# LOAD MODEL
# ==================================================

try:

    model = pickle.load(
        open("admission_model.pkl", "rb")
    )

    le_cat = pickle.load(
        open("category_encoder.pkl", "rb")
    )

    le_college = pickle.load(
        open("college_encoder.pkl", "rb")
    )

    le_branch = pickle.load(
        open("branch_encoder.pkl", "rb")
    )

    MODEL_READY = True

except:

    MODEL_READY = False

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("🎓 Merit Map")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "College Recommendation",
        "Admission Predictor",
        "Analytics",
        "Top Colleges"
    ]
)

# ==================================================
# HOME
# ==================================================

if page == "Home":

    st.title("🎓 Merit Map")

    st.markdown(
        """
        ### AI Powered College Recommendation System

        Features:
        - College Recommendation
        - Admission Prediction
        - Placement Analytics
        - Fee Analysis
        - NIRF Analysis
        """
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Colleges",
        df["college"].nunique()
    )

    c2.metric(
        "Branches",
        df["branch"].nunique()
    )

    c3.metric(
        "Records",
        len(df)
    )

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

# ==================================================
# COLLEGE RECOMMENDATION
# ==================================================

elif page == "College Recommendation":

    st.title("🎓 College Recommendation")

    rank = st.number_input(
        "Enter Your Rank",
        min_value=1,
        value=2000
    )

    category = st.selectbox(
        "Category",
        sorted(df["category"].unique())
    )

    branch = st.selectbox(
        "Branch",
        sorted(df["branch"].unique())
    )

    max_fee = st.slider(
        "Maximum Fees",
        int(df["Fees"].min()),
        int(df["Fees"].max()),
        int(df["Fees"].max())
    )

    result = df[
        (df["category"] == category)
        &
        (df["branch"] == branch)
        &
        (df["Cutoff_Rank"] >= rank)
        &
        (df["Fees"] <= max_fee)
    ]

    if st.button("Recommend Colleges"):

        if len(result) == 0:

            st.warning(
                "No colleges found."
            )

        else:

            result = result.sort_values(
                by="Recommendation_Score",
                ascending=False
            )

            st.success(
                f"{len(result)} colleges found"
            )

            st.dataframe(
                result[
                    [
                        "college",
                        "branch",
                        "Cutoff_Rank",
                        "Fees",
                        "Placement_Percentage",
                        "Average_Package",
                        "NIRF_Rank",
                        "Recommendation_Score"
                    ]
                ]
            )

            csv = result.to_csv(
                index=False
            )

            st.download_button(
                "Download CSV",
                csv,
                "recommendations.csv",
                "text/csv"
            )

# ==================================================
# ADMISSION PREDICTOR
# ==================================================

elif page == "Admission Predictor":

    st.title("🤖 Admission Predictor")

    if not MODEL_READY:

        st.error(
            "Model files not found."
        )

    else:

        rank = st.number_input(
            "Student Rank",
            min_value=1,
            value=2000
        )

        category = st.selectbox(
            "Category",
            sorted(df["category"].unique())
        )

        college = st.selectbox(
            "College",
            sorted(df["college"].unique())
        )

        branch = st.selectbox(
            "Branch",
            sorted(df["branch"].unique())
        )

        selected = df[
            (df["college"] == college)
            &
            (df["branch"] == branch)
        ]

        if len(selected) > 0:

            row = selected.iloc[0]

            if st.button("Predict Admission"):

                student = [[
                    rank,
                    le_cat.transform([category])[0],
                    le_college.transform([college])[0],
                    le_branch.transform([branch])[0],
                    row["Cutoff_Rank"],
                    row["Fees"],
                    row["Placement_Percentage"],
                    row["Average_Package"],
                    row["NIRF_Rank"],
                    row["Available_Seats"]
                ]]

                probability = model.predict_proba(
                    student
                )[0][1]

                st.success(
                    f"Admission Chance : {probability*100:.2f}%"
                )

# ==================================================
# ANALYTICS
# ==================================================

elif page == "Analytics":

    st.title("📊 Analytics Dashboard")

    tab1, tab2, tab3 = st.tabs(
        [
            "Placements",
            "Fees vs Package",
            "NIRF"
        ]
    )

    with tab1:

        fig = px.bar(
            df,
            x="college",
            y="Placement_Percentage",
            color="college",
            title="Placement Percentage"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with tab2:

        fig = px.scatter(
            df,
            x="Fees",
            y="Average_Package",
            color="college",
            size="Placement_Percentage",
            title="Fees vs Package"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with tab3:

        fig = px.bar(
            df,
            x="college",
            y="NIRF_Rank",
            color="college",
            title="NIRF Ranking"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# ==================================================
# TOP COLLEGES
# ==================================================

elif page == "Top Colleges":

    st.title("🏆 Top Colleges")

    top = df.sort_values(
        by="Recommendation_Score",
        ascending=False
    ).head(10)

    st.dataframe(
        top[
            [
                "college",
                "branch",
                "Recommendation_Score"
            ]
        ]
    )

    fig = px.bar(
        top,
        x="college",
        y="Recommendation_Score",
        color="college",
        title="Top Recommended Colleges"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
