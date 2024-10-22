from django import template

register = template.Library()


@register.filter()
def media_filter(data):
    if data:
        return f"/media/{data}"
    return "#"


@register.filter()
def text_cropping(value, length=100):
    if value is None:
        return ""  # или какое-то значение по умолчанию
    if len(value) > length:
        return value[:length] + "..."
    return value


@register.filter()
def add_class(value, arg):
    """
    Фильтр позвляет динамически добавлять CSS-классы к виджетам полей формы в Django-шаблоне
    """
    try:
        return value.as_widget(attrs={'class': arg})
    except AttributeError:
        return value
