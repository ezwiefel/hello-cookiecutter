<!--
 Copyright (c) 2021 Microsoft
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

# {{ cookiecutter.project_name }}

This is a sample cookiecutter template.

You've entered the following:
    * Project Name: {{ cookiecutter.project_name }}
    * Repo Name: {{ cookiecutter.repo_name }}
    * Name: {{ cookiecutter.name }}
    {% if cookiecutter.include_goodbye == "True" %}
    * You've included both the "Hello" and "Goodbye" modules
    {% else %}
    * You've only included the "Hello" module
    {% endif %}