from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 어떤 정보인지 편하게 알아보기 위해 사용
    def __str__(self):
        return self.title