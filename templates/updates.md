{% if added_filaments %}
**✅ Added filaments**

{% for filament in added_filaments %}
- {{ filament.as_markdown() }}
{% endfor %}
{% endif %}

{% if removed_filaments %}
**❌ Removed filaments**

{% for filament in removed_filaments %}
- {{ filament.as_markdown() }}
{% endfor %}
{% endif %}
