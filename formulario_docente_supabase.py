
import streamlit as st
from supabase import create_client, Client
import datetime

# Conexión a Supabase
SUPABASE_URL = "https://owfpruyynhwfwmoswtyx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im93ZnBydXl5bmh3Zndtb3N3dHl4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzNTAwNjQsImV4cCI6MjA2MzkyNjA2NH0.rH-vDwm02GTIftq-yT53a-mVcr43lPiOcD_F_NDErUU"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="Formulario Docente", page_icon="📋", layout="centered")
st.markdown("**Versión actualizada del formulario 2025 ✅**")

st.title("📋 Formulario de Seguimiento Docente")
st.markdown("Complete este formulario para registrar el seguimiento académico y de taller de los alumnos.")

with st.form("formulario_docente"):
    st.subheader("🧑‍🏫 Datos del estudiante")
    espacio_curricular = st.text_input("📚 Espacio Curricular")
    nombre_apellido = st.text_input("👤 Nombre y Apellido del Alumno")
    curso_y_division = st.text_input("🏫 Curso y División")
    edad = st.number_input("🎂 Edad", min_value=10, max_value=25, step=1)

    st.subheader("📘 Seguimiento Académico")
    cuenta_material = st.radio("¿Cuenta con el material didáctico necesario?", ["Sí", "No"])
    trabaja_en_clase = st.selectbox("Nivel de trabajo en clase", ["Alto", "Medio", "Bajo"])
    resolucion_tareas = st.radio("¿Resuelve las tareas asignadas?", ["Sí", "No"])
    tardanza_frecuente = st.radio("¿Llega tarde frecuentemente?", ["Sí", "No"])
    respeto_docente = st.radio("¿Respeta al docente?", ["Sí", "No"])
    estado_carpeta = st.selectbox("Estado de la carpeta o apuntes", ["Muy bien", "Regular", "Incompleta"])
    cantidad_faltas_conducta = st.number_input("Cantidad de faltas de conducta", min_value=0, step=1)
    cantidad_de_faltas = st.number_input("Cantidad total de inasistencias", min_value=0, step=1)
    trabajo_en_equipo = st.selectbox("Trabajo en equipo", ["Bueno", "Regular", "Malo"])
    interesado_en_clase = st.radio("¿Se muestra interesado en clase?", ["Sí", "No"])
    cumple_normas_convivencia = st.radio("¿Cumple con las normas de convivencia?", ["Sí", "No"])

    st.subheader("🛠️ Seguimiento en Taller")
    manejo_herramientas = st.selectbox("Manejo de herramientas y máquinas", ["Bueno", "Regular", "Malo"])
    usa_epp = st.radio("¿Usa elementos de protección personal? (ámbito taller)", ["Sí", "No"])
    trae_material_taller = st.radio("¿Trae el material para trabajar en taller?", ["Sí", "No"])

    submitted = st.form_submit_button("✅ Enviar")
    if submitted:
        # Validar campos obligatorios
        campos_obligatorios = {
            "Espacio Curricular": espacio_curricular,
            "Nombre y Apellido": nombre_apellido,
            "Curso y División": curso_y_division
        }
        campos_faltantes = [campo for campo, valor in campos_obligatorios.items() if not valor.strip()]

        if campos_faltantes:
            st.error(f"⚠️ Por favor completá los siguientes campos obligatorios: {', '.join(campos_faltantes)}")
        else:
            data = {
                "espacio_curricular": espacio_curricular.strip(),
                "nombre_apellido": nombre_apellido.strip(),
                "curso_y_division": curso_y_division.strip(),
                "edad": edad,
                "cuenta_material": cuenta_material,
                "trabaja_en_clase": trabaja_en_clase,
                "resolucion_tareas": resolucion_tareas,
                "tardanza_frecuente": tardanza_frecuente,
                "respeto_docente": respeto_docente,
                "estado_carpeta": estado_carpeta,
                "cantidad_faltas_conducta": cantidad_faltas_conducta,
                "cantidad_de_faltas": cantidad_de_faltas,
                "trabajo_en_equipo": trabajo_en_equipo,
                "interesado_en_clase": interesado_en_clase,
                "cumple_normas_convivencia": cumple_normas_convivencia,
                "manejo_herramientas": manejo_herramientas,
                "usa_epp": usa_epp,
                "trae_material_taller": trae_material_taller,
                #"fecha": datetime.datetime.now().isoformat()
            }

            try:
                supabase.table("formulario_docente").insert(data).execute()
                st.success("✅ Los datos han sido registrados correctamente.")
            except Exception as e:
                st.error(f"❌ Error al registrar los datos: {e}")

