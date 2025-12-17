import streamlit as st
from core.generator import generate_reaction
from core.validator import validate_solution
from core.reaction import to_latex

def exercise_view():

    REACTION_TYPES = {
    "Metal Oxides": "metal_oxide",
    "Metal Non-Metal": "metal_nonmetal",
    "Combustion": "combustion",
    "Acid-Base Neutralization": "acid_base",
    }

    st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #1f77b4;  /* Blue color */
        color: white;                /* Text color */
        height: 50px;                /* Taller button */
        width: 100%;                 /* Full width of container */
        font-size: 20px;             /* Bigger text */
        border-radius: 10px;         /* Rounded corners */
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    # --- 2. Sidebar for selecting reaction types ---
    st.sidebar.subheader("Choose reaction types")

    selected_types = []
    for i, (name, key) in enumerate(REACTION_TYPES.items()):
        default_value = True if i == 0 else False
        if st.sidebar.checkbox(name, value=default_value):
            selected_types.append(key)
    
    if "reaction" not in st.session_state:
        st.session_state.reaction = generate_reaction(selected_types)
    
    if "new_reaction" not in st.session_state:
        st.session_state.new_reaction = True
    
    if "reaction_id" not in st.session_state:
        st.session_state.reaction_id = 0

    # --- New reaction ---
    col1, col2, col3 = st.columns([2, 1, 2])  # center column is twice as wide
    with col2:
        if st.button("New Reaction"):
            st.session_state.reaction_id += 1
            st.session_state.reaction = generate_reaction(selected_types)    

    rid = st.session_state.reaction_id
    reaction = st.session_state.reaction

    total_compounds = reaction.reactants + reaction.products
    user_coeffs = []

    st.subheader("Balance the reaction")

    # --- Prepare the column structure ---
    # Number of columns: 2 per compound (input + formula) + number of plus signs + arrow
    num_plus = len(reaction.reactants) - 1 + len(reaction.products) - 1
    num_arrow = 1
    num_cols = len(total_compounds) * 2 + num_plus + num_arrow
    cols = st.columns(num_cols)

    #for i, col in enumerate(cols):
    #    col.markdown(
    #        f"<div style='background-color: rgba(255,0,0,0.2); height:50px'>Column {i}</div>",
    #        unsafe_allow_html=True
    #    )

    col_idx = 0

    # --- Reactants ---
    for i, reactant in enumerate(reaction.reactants):
        # Input box

        val = cols[col_idx].text_input(label="", key=f"r{i}_{rid}", placeholder="?")
        user_coeffs.append(val)
        col_idx += 1

        # Compound
        cols[col_idx].markdown("<br style='line-height:1.0'>", unsafe_allow_html=True) #pushes text up?
        cols[col_idx].latex(to_latex(reactant))
        col_idx += 1

        # Plus sign between reactants
        if i < len(reaction.reactants) - 1:
            cols[col_idx].markdown("<br style='line-height:1.0'>", unsafe_allow_html=True) #pushes text up?
            cols[col_idx].latex("+")
            col_idx += 1

    # --- Arrow ---
    cols[col_idx].markdown("<br style='line-height:1.0'>", unsafe_allow_html=True) #pushes text up?
    cols[col_idx].latex(r"\longrightarrow")
    col_idx += 1

    # --- Products ---
    for i, product in enumerate(reaction.products):
        val = cols[col_idx].text_input(label="", key=f"p{i}_{rid}", placeholder="?")
        user_coeffs.append(val)
        col_idx += 1

        cols[col_idx].markdown("<br style='line-height:1.0'>", unsafe_allow_html=True) #pushes text up?
        cols[col_idx].latex(to_latex(product))
        col_idx += 1

        # Plus sign between products
        if i < len(reaction.products) - 1:
            cols[col_idx].markdown("<br style='line-height:1.0'>", unsafe_allow_html=True) #pushes text up?
            cols[col_idx].latex("+")
            col_idx += 1


    
    # --- Buttons ---
    # --- Check button ---
    if st.button("Check answer", key=f"check_reaction_button_{rid}"):
        user_input = ",".join(user_coeffs)
        if validate_solution(user_input, reaction.solution):
            st.success("Correct! 🎉")
        else:
            st.error("Incorrect, try again!")

    