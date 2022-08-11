Available prusament filaments:

{% for filament in filaments %}
- {{ filament.as_markdown() }}
{% endfor %}

{% include 'footer.md' %}
