import streamlit as st
import numpy as np
import pandas as pd
import libreria_funciones as lf
import libreria_funciones_proyecto1 as lfp
from librería_clases_proyecto1 import Paciente

##Elaboracion de sidebar
st.sidebar.title("Paginas")
st.sidebar.image("DMC.png",width =250)

##Creacion de tema/logo pagina
st.image("Logo_proyecto.png",width =2000)
st.write("Elaborado por: Harold Hernandez")

modulos = st.sidebar.selectbox("Selecione el módulo",["Home","Ejercicio1", "Ejercicio2", "Ejercicio3", "Ejercicio4"])

#####################################################################################################################
####### MODULO HOME
######################################################################################################################

if modulos == "Home":

  st.subheader("APLICACIÓN EN STREAMLIT")
  st.markdown("**Nombre:** Harold Hernandez Medina")
  st.markdown("**Modulo:**  Python Fundamentals")
  st.markdown("**Edad:**  25 años")
  st.markdown("**Año:**  2026")
  st.markdown("**Descripcion:**  Una aplicación interactiva en Streamlit integrando los contenidos revisados en el módulo")
  st.markdown("**Tecnologias:**  GitHub,Streamlit,Python")

######################################################################################################################
####### EJERCICIO 1
######################################################################################################################

elif modulos == "Ejercicio1":
  st.subheader("EJERCICIO 1")
  
  # Inicializar la lista vacía en la sesión de Streamlit para no perder los datos
  if "movimientos" not in st.session_state:
      st.session_state.movimientos = []
  
  # --- DESCRIPCIÓN CON ST.MARKDOWN() ---
  st.markdown("""
  # Registro de Movimientos Financieros
  En este módulo podrás registrar tus ingresos y gastos de manera rápida. 
  Ingresa el concepto, selecciona el tipo de movimiento y coloca el valor. 
  Al presionar el botón, el registro se agregará a la lista y se calculará el flujo de caja final.
  """)
  
  # --- WIDGETS PARA INGRESAR DATOS ---
  concepto = st.text_input("Ingresa el concepto:")
  tipo = st.selectbox("Selecciona el tipo de movimiento:", ["Ingreso", "Gasto"])
  valor = st.number_input("Ingresa el valor:", min_value=0.0)
  
  # --- BOTÓN PARA AGREGAR MOVIMIENTOS ---
  if st.button("Agregar movimiento"):
      # Se agrega el movimiento como un diccionario a la lista
      st.session_state.movimientos.append(
          {"concepto": concepto, "tipo": tipo, "valor": valor}
      )
  
  # --- MOSTRAR LISTA DE MOVIMIENTOS ---
  st.subheader("Lista de movimientos registrados:")
  st.dataframe(st.session_state.movimientos)
  
  # --- CÁLCULO DE TOTALES Y SALDO FINAL ---
  total_ingresos = 0.0
  total_gastos = 0.0
  
  for movimiento in st.session_state.movimientos:
      if movimiento["tipo"] == "Ingreso":
          total_ingresos += movimiento["valor"]
      else:
          total_gastos += movimiento["valor"]
  
  saldo_final = total_ingresos - total_gastos
  
  # --- RESULTADOS Y MÉTRICAS ---
  st.metric("Total Ingresos", total_ingresos)
  st.metric("Total Gastos", total_gastos)
  st.metric("Saldo Final", saldo_final)
  
  # --- INDICADOR DEL FLUJO DE CAJA ---
  if saldo_final >= 0:
      st.success("El flujo de caja está: A FAVOR")
  else:
      st.error("El flujo de caja está: EN CONTRA") 

######################################################################################################################
####### EJERCICIO 2
######################################################################################################################


elif modulos == "Ejercicio2":
  st.subheader("EJERCICIO 2")
  # Inicializar los arreglos de NumPy en la sesión de Streamlit
  if "nombres" not in st.session_state:
      st.session_state.nombres = np.array([])
      st.session_state.categorias = np.array([])
      st.session_state.precios = np.array([])
      st.session_state.cantidades = np.array([])
      st.session_state.totales = np.array([])
  
  # --- DESCRIPCIÓN DEL EJERCICIO CON ST.MARKDOWN() ---
  st.markdown("""
  # Registro de Productos y Ventas
  En este ejercicio se registra la información de productos utilizando arreglos de NumPy.
  Ingresa el nombre, la categoría, el precio y la cantidad. El total se calculará automáticamente
  y la tabla en DataFrame se actualizará al agregar el registro.
  """)
  
  # --- FORMULARIO DE INGRESO DE DATOS ---
  nombre = st.text_input("Nombre del producto:")
  categoria = st.selectbox(
      "Categoría:", ["Electrónica", "Ropa", "Alimentos", "Otros"]
  )
  precio = st.number_input("Precio:", min_value=0.0)
  cantidad = st.number_input("Cantidad:", min_value=0, step=1)
  
  # Cálculo automático del total
  total = precio * cantidad
  
  # --- BOTÓN PARA AGREGAR NUEVO REGISTRO ---
  if st.button("Agregar producto"):
      # Agregar los datos a cada array de NumPy usando np.append
      st.session_state.nombres = np.append(st.session_state.nombres, nombre)
      st.session_state.categorias = np.append(
          st.session_state.categorias, categoria
      )
      st.session_state.precios = np.append(st.session_state.precios, precio)
      st.session_state.cantidades = np.append(
          st.session_state.cantidades, cantidad
      )
      st.session_state.totales = np.append(st.session_state.totales, total)
  
  # --- CONVERSIÓN DE ARREGLOS DE NUMPY A DATAFRAME Y MUESTRA EN PANTALLA ---
  df_productos = pd.DataFrame({
      "Producto": st.session_state.nombres,
      "Categoría": st.session_state.categorias,
      "Precio": st.session_state.precios,
      "Cantidad": st.session_state.cantidades,
      "Total": st.session_state.totales,
  })
  
  # Mostrar la tabla en DataFrame actualizada
  st.dataframe(df_productos)  

######################################################################################################################
####### EJERCICIO 3
######################################################################################################################

elif modulos == "Ejercicio3":
  # --- FUNCIONES DE VALIDACIÓN Y CÁLCULO PROPORCIONADAS ---
  def validar_positivo(valor: float, nombre: str):
      if valor <= 0:
          raise ValueError(f"El parámetro {nombre} debe ser mayor a 0.")
  
  
  def validar_porcentaje(valor: float, nombre: str):
      if valor < 0:
          raise ValueError(f"El parámetro {nombre} no puede ser negativo.")
  
  # --- INICIALIZAR EL HISTÓRICO EN LA SESIÓN ---
  if "historico" not in st.session_state:
      st.session_state.historico = []
  
  # --- SELECTOR DE FUNCIÓN ---
  opcion_funcion = st.selectbox(
      "Selecciona la función a ejecutar:",
      ["Calcular Cuota Préstamo (Sistema Francés)"],
  )
  
  # --- WIDGETS PARA INGRESAR PARÁMETROS ---
  monto = st.number_input("Monto del préstamo:", min_value=0.0, value=10000.0)
  tasa_anual_pct = st.number_input(
      "Tasa anual (%):", min_value=0.0, value=12.0
  )
  plazo_meses = st.number_input(
      "Plazo en meses:", min_value=1, value=12, step=1
  )
  
  # --- BOTÓN PARA EJECUTAR Y MOSTRAR RESULTADOS ---
  if st.button("Ejecutar"):
      resultado = lfp.calcular_cuota_prestamo_frances(
          monto, tasa_anual_pct, int(plazo_meses)
      )
  
      # Mostrar el resultado en pantalla usando st.write()
      st.write("### Resultado de la simulación:")
      st.write("Cuota Mensual:", resultado["cuota_mensual"])
      st.write("Total Pagado:", resultado["total_pagado"])
      st.write("Interés Total:", resultado["interes_total"])
  
      # Guardar en el histórico
      registro = {
          "Monto": monto,
          "Tasa Anual (%)": tasa_anual_pct,
          "Plazo (Meses)": int(plazo_meses),
          "Cuota Mensual": resultado["cuota_mensual"],
          "Total Pagado": resultado["total_pagado"],
          "Interés Total": resultado["interes_total"],
      }
      st.session_state.historico.append(registro)
  
  # --- TABLA HISTÓRICA DE RESULTADOS OBTENIDOS ---
  st.write("### Histórico de resultados obtenidos")
  st.dataframe(pd.DataFrame(st.session_state.historico))
  
######################################################################################################################
####### EJERCICIO 4
######################################################################################################################
 
else:
  st.subheader("EJERCICIO 4")
  def validar_positivo(valor: float, nombre: str):
      if valor <= 0:
          raise ValueError(f"El parámetro {nombre} debe ser mayor a 0.")

  # --- INICIALIZAR LA LISTA DE PACIENTES EN LA SESIÓN ---
  if "pacientes" not in st.session_state:
      st.session_state.pacientes = []
  
  # --- PESTAÑAS PARA EL CRUD (st.tabs) ---
  tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(
      ["Crear", "Leer", "Actualizar", "Eliminar"]
  )
  
  # =========================================================
  # 1. CREAR PACIENTE
  # =========================================================
  with tab_crear:
      nombre = st.text_input("Nombre del paciente:")
      peso_kg = st.number_input("Peso (kg):", min_value=0.0, value=70.0)
      altura_m = st.number_input("Altura (m):", min_value=0.0, value=1.70)
  
      if st.button("Crear registro"):
          if nombre != "" and peso_kg > 0 and altura_m > 0:
              nuevo_paciente = Paciente(nombre, peso_kg, altura_m)
              st.session_state.pacientes.append(nuevo_paciente)
  
  # =========================================================
  # 2. LEER / VISUALIZAR REGISTROS
  # =========================================================
  with tab_leer:
      registros = [p.resumen() for p in st.session_state.pacientes]
      st.dataframe(pd.DataFrame(registros))
  
  # =========================================================
  # 3. ACTUALIZAR REGISTRO
  # =========================================================
  with tab_actualizar:
      nombres_pacientes = [p.nombre for p in st.session_state.pacientes]
      paciente_sel = st.selectbox(
          "Selecciona el paciente a actualizar:",
          [""] + nombres_pacientes,
          key="sb_act",
      )
  
      if paciente_sel != "":
          # Buscar el objeto paciente seleccionado
          index = nombres_pacientes.index(paciente_sel)
          p_obj = st.session_state.pacientes[index]
  
          nuevo_nombre = st.text_input("Nuevo nombre:", value=p_obj.nombre)
          nuevo_peso = st.number_input(
              "Nuevo peso (kg):", min_value=0.0, value=p_obj.peso_kg
          )
          nueva_altura = st.number_input(
              "Nueva altura (m):", min_value=0.0, value=p_obj.altura_m
          )
  
          if st.button("Actualizar registro"):
              if nuevo_nombre != "" and nuevo_peso > 0 and nueva_altura > 0:
                  p_actualizado = Paciente(
                      nuevo_nombre, nuevo_peso, nueva_altura
                  )
                  st.session_state.pacientes[index] = p_actualizado
  
  # =========================================================
  # 4. ELIMINAR REGISTRO
  # =========================================================
  with tab_eliminar:
      nombres_pacientes_del = [p.nombre for p in st.session_state.pacientes]
      paciente_elim = st.selectbox(
          "Selecciona el paciente a eliminar:",
          [""] + nombres_pacientes_del,
          key="sb_del",
      )
  
      if st.button("Eliminar registro"):
          if paciente_elim != "":
              index_del = nombres_pacientes_del.index(paciente_elim)
              st.session_state.pacientes.pop(index_del)
  
