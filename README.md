<p align="center"><img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3E%3Cpath d='M14.135 4H18.1v18.169a26.218 26.218 0 0 1-5.143.535c-4.842-.005-7.362-2.168-7.362-6.322 0-4 2.673-6.6 6.816-6.6a6.448 6.448 0 0 1 1.724.2V4Zm0 9.142a3.992 3.992 0 0 0-1.337-.2c-2 0-3.163 1.223-3.163 3.366 0 2.087 1.107 3.239 3.138 3.239a9.355 9.355 0 0 0 1.362-.1v-6.3Z' style='fill:%2344b78b'/%3E%3Cpath d='M24.4 10.059v9.1c0 3.133-.235 4.639-.923 5.938A6.316 6.316 0 0 1 20.237 28l-3.678-1.733a5.708 5.708 0 0 0 3.141-2.629c.566-1.121.745-2.42.745-5.837v-7.742ZM20.441 4.02h3.964v4.028h-3.964z' style='fill:%2344b78b'/%3E%3C/svg%3E" width="128" height="128"></p>


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
