from setuptools import setup

setup(name="ln.py",
      version="0.3",
      description="symlinks made easier",
      url="https://github.com/dmerejkowsky/ln.py",
      author="Dimitri Merejkowsky",
      author_email="d.merej@gmail.com",
      py_modules=["ln"],
      entry_points={
        "console_scripts": [
          "lnp = ln:main",
        ]
      },
      classifiers=[
          "Programming Language :: Python :: 3 :: Only",
          "Environment :: Console",
          "Topic :: System :: Shells",
          "License :: OSI Approved :: BSD License",
    ]
)
