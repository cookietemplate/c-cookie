add_executable(app_{{ cookiecutter.project_slug }}
        main.c
)
target_link_libraries(app_{{ cookiecutter.project_slug }} {{ cookiecutter.project_slug }})
