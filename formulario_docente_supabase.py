
import streamlit as st
from supabase import create_client

# Configuración de Supabase
SUPABASE_URL = "https://owfpruyynhwfwmoswtyx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im93ZnBydXl5bmh3Zndtb3N3dHl4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDgzNTAwNjQsImV4cCI6MjA2MzkyNjA2NH0.rH-vDwm02GTIftq-yT53a-mVcr43lPiOcD_F_NDErUU"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("Formulario Docente - Registro de Seguimiento de Alumnos")

with st.form("formulario_seguimiento"):
    espacio_curricular = st.text_input("Espacio Curricular")
    nombre_apellido = st.text_input("Nombre y Apellido del Alumno")
    curso_y_division = st.text_input("Curso y División")
    edad = st.number_input("Edad", min_value=10, max_value=25, step=1)

    cuenta_material = st.radio("¿Cuenta con el material didáctico necesario?", ["Sí", "No"])
    trabaja_en_clase = st.selectbox("Participación en clase", ["Alto", "Medio", "Bajo"])
    resolucion_tareas = st.radio("¿Resuelve tareas?", ["Sí", "No"])
    tardanza_frecuente = st.radio("¿Tiene tardanzas frecuentes?", ["Sí", "No"])
    respeto_docente = st.radio("¿Respeta al docente?", ["Sí", "No"])
    estado_carpeta = st.selectbox("Estado de carpeta/apuntes", ["Muy bien", "Regular", "Incompleta"])
    cantidad_faltas_conducta = st.number_input("Cantidad de faltas de conducta", min_value=0, step=1)
    trabajo_en_equipo = st.selectbox("Trabajo en equipo", ["Bueno", "Regular", "Malo"])
    interesado_en_clase = st.radio("¿Se muestra interesado en clase?", ["Sí", "No"])
    manejo_herramientas = st.selectbox("Manejo de herramientas y máquinas", ["Bueno", "Regular", "Malo"])
    usa_epp = st.radio("¿Usa elementos de protección personal?", ["Sí", "No"])
    trae_material_taller = st.radio("¿Trae el material al taller?", ["Sí", "No"])
    cumple_normas_convivencia = st.radio("¿Cumple con las normas de convivencia?", ["Sí", "No"])
    cantidad_de_faltas = st.number_input("Cantidad de faltas", min_value=0, step=1)

    submit = st.form_submit_button("Enviar")

    if submit:
        data = {
            "espacio_curricular": espacio_curricular,
            "nombre_apellido": nombre_apellido,
            "curso_y_division": curso_y_division,
            "edad": edad,
            "cuenta_material": cuenta_material,
            "trabaja_en_clase": trabaja_en_clase,
            "resolucion_tareas": resolucion_tareas,
            "tardanza_frecuente": tardanza_frecuente,
            "respeto_docente": respeto_docente,
            "estado_carpeta": estado_carpeta,
            "cantidad_faltas_conducta": cantidad_faltas_conducta,
            "trabajo_en_equipo": trabajo_en_equipo,
            "interesado_en_clase": interesado_en_clase,
            "manejo_herramientas": manejo_herramientas,
            "usa_epp": usa_epp,
            "trae_material_taller": trae_material_taller,
            "cumple_normas_convivencia": cumple_normas_convivencia,
            "cantidad_de_faltas": cantidad_de_faltas,
        }
        supabase.table("formulario_docente").insert(data).execute()
        st.success("✅ Datos enviados correctamente")
