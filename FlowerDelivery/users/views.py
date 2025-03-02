from django.views.generic import FormView
from django.contrib.auth import login
from .forms import UserRegistrationForm

class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = '/'
    success_message = 'Вы успешно зарегистрировались'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Авторизуем пользователя после регистрации
        return super().form_valid(form)
# Create your views here.
