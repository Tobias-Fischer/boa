import pathlib
from subprocess import check_call


def test_build_recipes():
    recipes_dir = pathlib.Path(__file__).parent / "recipes"

    recipes = [str(x) for x in recipes_dir.iterdir() if x.is_dir()]

    for recipe in recipes:
        check_call(["conda", "mambabuild", recipe])


def test_build_notest():
    recipes_dir = pathlib.Path(__file__).parent / "recipes"

    recipes = [str(x) for x in recipes_dir.iterdir() if x.is_dir()]
    recipe = recipes[0]

    check_call(["conda", "mambabuild", recipe, "--no-test"])
