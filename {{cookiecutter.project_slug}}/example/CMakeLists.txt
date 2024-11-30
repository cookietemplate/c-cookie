add_executable(example_{{ cookiecutter.project_slug }}
        main.c
)
target_link_libraries(example_{{ cookiecutter.project_slug }} {{ cookiecutter.project_slug }})
