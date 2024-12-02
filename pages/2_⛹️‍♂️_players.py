import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="Players",
    layout="wide"
)

# DATA
df_data = st.session_state["data"]

# SELECT CLUBS
clubs = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Club", clubs)

# SELECT PLAYERS
df_players = df_data[(df_data["Club"] == club)]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Player", players)

# STATS
player_stats = df_data[df_data["Name"] == player].iloc[0]

# IMAGE/NAME
st.image(player_stats["Photo"])
st.title(player_stats["Name"])

# CLUB/POSITION
st.markdown(f"**Club:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

# AGE/HEIGHT/WEIGHT
col1, col2, col3 = st.columns(3)
col1.markdown(f"**Age** {player_stats['Age']}")
col2.markdown(f"**Height** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Weight** {player_stats['Weight(lbs.)'] * 0.453:.2f}")
st.divider()

# OVERALL
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

# METRICS
col1, col2, col3 = st.columns(3)
col1.metric(label="Value", value=f"£ {player_stats['Value(£)']}")
col2.metric(label="Wage", value=f"£ {player_stats['Wage(£)']}")
col3.metric(label="Release Clause", value=f"£ {player_stats['Release Clause(£)']}")
