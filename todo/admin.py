from django.contrib import admin
from todo.models import Todo, Comment

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_completed', 'start_date', 'end_date')
    list_filter = ('is_completed',)
    search_fields = ('title',) #검색 필터
    ordering = ('id',)  #정렬 방식 (앞에 - 를 붙이면 DESC, Default=ASC)
    fieldsets = ( # 특정 레코드 추가/수정할 때 나오는 폼의 필드 순서 및 표시
        ('Todo Info', {
            'fields': ('title', 'description', 'is_completed')
        }),
        ('Date Range', {
            'fields': ('start_date', 'end_date')
        }),
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'updated_at')
    list_filter = ('user', 'message',)
    search_fields = ('message',)
    ordering = ('id',)  # 정렬 방식 (앞에 - 를 붙이면 DESC, Default=ASC)