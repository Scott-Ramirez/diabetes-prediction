<p align="center">
  <a href="https://www.djangoproject.com/" target="blank"><img src="https://svgl.app/library/django.svg" width="200" alt="Django Logo" /></a>
</p>



# Proyecto de Predicción de Diabetes

Este proyecto consiste en una aplicación web para la predicción de la diabetes. Utiliza un modelo de aprendizaje automático para predecir la probabilidad de desarrollar diabetes en el futuro basado en varios factores de riesgo.

## Descripción del Proyecto

La aplicación web consta de las siguientes secciones principales:

1. **Inicio**: Página de bienvenida donde los usuarios son recibidos con información sobre la aplicación y un enlace para acceder al formulario de predicción.

2. **Formulario de Predicción**: Los usuarios pueden ingresar su información personal, como edad, género, peso, altura y nivel de glucemia en ayunas, y luego hacer clic en el botón de predicción para obtener el resultado de la predicción.

3. **Resultados de la Predicción**: Después de completar el formulario, los usuarios son dirigidos a una página que muestra los resultados de la predicción. Dependiendo del resultado, se les informa si es posible que desarrollen diabetes en el futuro y se les proporcionan recomendaciones correspondientes.

4. **Información sobre la Diabetes**: Sección que proporciona información detallada sobre la diabetes, incluyendo definición, tipos, síntomas, factores de riesgo y complicaciones asociadas.

5. **Cuidado de la Salud**: Ofrece consejos y recomendaciones sobre cómo cuidar la salud para controlar la diabetes y prevenir complicaciones.

6. **Prevención de la Diabetes**: Proporciona estrategias y medidas preventivas que los usuarios pueden tomar para reducir el riesgo de desarrollar diabetes tipo 2 o retrasar su progresión.

## Tecnologías Utilizadas

- **Frontend**: Se utiliza HTML, CSS y Bootstrap para la estructura y el diseño de la interfaz de usuario.
- **Backend**: Se emplea un framework de desarrollo web, como Django o Flask, para la lógica del servidor y la comunicación con el modelo de aprendizaje automático.
- **Modelo de Aprendizaje Automático**: Se utiliza un modelo de aprendizaje automático previamente entrenado para realizar la predicción de la diabetes.
- **Librerías y Herramientas**: Se pueden utilizar diversas librerías y herramientas adicionales dependiendo de los requisitos específicos del proyecto, como TensorFlow para el desarrollo del modelo de aprendizaje automático y scikit-learn para el preprocesamiento de datos.

## Instrucciones de Uso

Para utilizar la aplicación, los usuarios simplemente deben completar el formulario de predicción con su información personal y hacer clic en el botón de predicción. Los resultados de la predicción se mostrarán en la siguiente página, junto con recomendaciones y consejos adicionales.

## Contribución

Si deseas contribuir al proyecto, puedes hacerlo abriendo un "issue" para discutir nuevos cambios o enviando una "pull request" con tus contribuciones propuestas.

## Pasos para Ejecutar el Proyecto

1. Clona este repositorio en tu máquina local usando el siguiente comando:

```
git clone https://github.com/Scott-Ramirez/diabetes-prediction.git
```
2. Asegúrate de tener R instalado en tu sistema. Puedes descargar R desde el sitio oficial de R.

3. Si el PATH de R no se agrega automáticamente durante la instalación, debes agregarlo manualmente a tu sistema para que la aplicación pueda ejecutarse correctamente. Puedes encontrar instrucciones detalladas sobre cómo agregar el PATH de R en la documentación oficial de R.


4. Ejecuta la aplicación web utilizando el siguiente comando:

```
python manage.py runserver
```


5. Abre tu navegador web y accede a la URL proporcionada por el servidor local para utilizar la aplicación.

¡Gracias por tu interés en este proyecto y por contribuir a mejorar la salud y el bienestar de las personas!
