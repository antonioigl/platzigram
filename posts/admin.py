"""Posts model."""

# Django
from django.contrib import admin

# Models
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('id', 'user', 'title', 'photo')
    list_display_links = ('id', 'user')
    list_editable = ('title', 'photo')
    search_fields = ('title', 'user__username', 'user__email')
    list_filter = ('created', 'modified')

    fieldsets = (
        ('Post', {
            'fields': (
                (('user'),),
                ('title', 'photo'),
            ),
        }),
        ('Metadata', {
            'fields':
                (('created', 'modified'),),
        }),
    )

    readonly_fields = ('created', 'modified',)

