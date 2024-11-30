add_executable(test_{{ cookiecutter.project_slug }} test_example.c)
target_link_libraries(test_{{ cookiecutter.project_slug }} {{ cookiecutter.project_slug }})
add_test(NAME test_{{ cookiecutter.project_slug }} COMMAND test_{{ cookiecutter.project_slug }})
