import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.set_page_config(page_title="EDA – Welcome Survey", layout="wide")

st.title("📊 Ankieta powitalna")

# --- WCZYTANIE PLIKU ---
st.sidebar.header("Ustawienia")

uploaded_file = st.sidebar.file_uploader(
    "Wgraj plik CSV", 
    type=['csv']
)

if uploaded_file:
    df = pd.read_csv(uploaded_file, sep=';')
    st.success("Plik został poprawnie wczytany!")

    st.subheader("🔍 Podgląd danych")
    st.dataframe(df.head())


    # --- INFO ---
   
    with st.expander("📌 Informacje o danych"):
        from io import StringIO

        buffer = StringIO()
        df.info(buf=buffer)
        info_str = buffer.getvalue()
        st.text(info_str)

        
        

    # --- OPIS STATYSTYCZNY ---
    st.subheader("📈 Opis statystyczny")
    st.dataframe(df.describe(include='all'))

    # --- BRAKI DANYCH ---
    st.subheader("🧩 Brakujące wartości")
    #na_series = df.isna().sum()
    #st.write(na_series)
    na_df = df.isna().sum().to_frame(name="missing_values").reset_index(names="column")
    st.dataframe(na_df, use_container_width=False)   # ⬅ tabela będzie wąska


    fig, ax = plt.subplots(figsize=(12,4))
    na_df.plot(kind='bar', ax=ax)
    ax.set_title("Braki danych w kolumnach")
    st.pyplot(fig)

    # --- ZMIENNE KATEGORYCZNE ---
    st.subheader("🟦 Analiza zmiennych kategorycznych")
    cat_cols = df.select_dtypes(include=['object']).columns

    selected_cat = st.selectbox("Wybierz zmienną kategoryczną:", cat_cols)

    fig, ax = plt.subplots(figsize=(8,4))
    df[selected_cat].value_counts(dropna=False).plot(kind='bar', ax=ax)
    ax.set_title(f"Rozkład zmiennej: {selected_cat}")
    st.pyplot(fig)

    # --- ZMIENNE NUMERYCZNE ---
    st.subheader("🟩 Analiza zmiennych liczbowych")
    num_cols = df.select_dtypes(include=[np.number]).columns

    if len(num_cols) > 0:
        selected_num = st.selectbox("Wybierz zmienną numeryczną:", num_cols)

        fig, ax = plt.subplots(figsize=(8,4))
        ax.hist(df[selected_num].dropna(), bins=10)
        ax.set_title(f"Histogram: {selected_num}")
        st.pyplot(fig)

    # --- KORELACJE ---
    st.subheader("🔗 Korelacje (zmienne numeryczne)")

    if len(num_cols) > 1:
        corr = df[num_cols].corr()

        fig, ax = plt.subplots(figsize=(10,6))
        cax = ax.matshow(corr, cmap='coolwarm')
        fig.colorbar(cax)

        ax.set_xticks(range(len(num_cols)))
        ax.set_xticklabels(num_cols, rotation=45)
        ax.set_yticks(range(len(num_cols)))
        ax.set_yticklabels(num_cols)

        st.pyplot(fig)

        # --- FILTRY UŻYTKOWNIKA ---

        st.subheader("🔎 Filtrowanie danych")

        # Tworzymy kolumny do estetycznego wyglądu
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            filter_age = st.multiselect(
                "Wiek",
                options=sorted(df['age'].dropna().unique()),
                default=[]
            )

        with col2:
            filter_edu = st.multiselect(
                "Wykształcenie",
                options=sorted(df['edu_level'].dropna().unique()),
                default=[]
            )

        with col3:
            filter_animal = st.multiselect(
                "Ulubione zwierzę",
                options=sorted(df['fav_animals'].dropna().unique()),
                default=[]
            )

        with col4:
            filter_place = st.multiselect(
                "Ulubione miejsce",
                options=sorted(df['fav_place'].dropna().unique()),
                default=[]
            )

        with col5:
            filter_industry = st.multiselect(
                "Branża",
                options=sorted(df['industry'].dropna().unique()),
                default=[]
            )

        # --- ZASTOSOWANIE FILTRÓW ---

        filtered_df = df.copy()

        if filter_age:
            filtered_df = filtered_df[filtered_df['age'].isin(filter_age)]

        if filter_edu:
            filtered_df = filtered_df[filtered_df['edu_level'].isin(filter_edu)]

        if filter_animal:
            filtered_df = filtered_df[filtered_df['fav_animals'].isin(filter_animal)]

        if filter_place:
            filtered_df = filtered_df[filtered_df['fav_place'].isin(filter_place)]

        if filter_industry:
            filtered_df = filtered_df[filtered_df['industry'].isin(filter_industry)]

        # --- WYNIK FILTROWANIA ---

        st.subheader("📋 Wyniki filtrowania")
        st.write(f"Liczba rekordów po filtrach: **{len(filtered_df)}**")

        st.dataframe(filtered_df)



    else:
        st.info("Brak wystarczającej liczby zmiennych numerycznych do analizy korelacji.")

else:
    st.warning("Proszę wgrać plik CSV po lewej stronie.")

