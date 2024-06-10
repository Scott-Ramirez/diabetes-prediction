import subprocess
from django.shortcuts import render
from .forms import DiabetesPredictionForm

def predict_diabetes(request):
    if request.method == 'POST':
        form = DiabetesPredictionForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            fasting_glucose = form.cleaned_data['fasting_glucose']
            
            # Ejecutar el script de R
            try:
                result = subprocess.run(
                    ['Rscript', 'r_scripts/prediccion_diabetes.R', str(age), gender, str(weight), str(height), str(fasting_glucose)],
                    capture_output=True, text=True, check=True
                )
                prediction_output = result.stdout.strip()
                
                # Interpretar el resultado de la predicción
                if "Es posible que pueda tener diabetes en el futuro." in prediction_output:
                    prediction_message = "Es posible que pueda tener diabetes en el futuro. Por favor, consulte a su médico."
                elif "Es poco probable que tenga diabetes en el futuro." in prediction_output:
                    prediction_message = "Es poco probable que tenga diabetes en el futuro. Continúe con su estilo de vida saludable."
                else:
                    prediction_message = f"Error inesperado en la predicción: {prediction_output}"
            except subprocess.CalledProcessError as e:
                prediction_message = f"Error en la predicción: {e.output}"
            
            return render(request, 'prediction_interface/results.html', {
                'age': age,
                'gender': gender,
                'weight': weight,
                'height': height,
                'fasting_glucose': fasting_glucose,
                'prediction': prediction_message
            })
    else:
        form = DiabetesPredictionForm()
    return render(request, 'prediction_interface/predict_diabetes.html', {'form': form})




def welcome(request):
    return render(request, 'prediction_interface/welcome.html')
