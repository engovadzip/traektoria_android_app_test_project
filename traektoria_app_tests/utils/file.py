def abs_path_from_project(relative_path: str):
    import traektoria_app_tests
    from pathlib import Path

    return (
        Path(traektoria_app_tests.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )