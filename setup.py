from setuptools import setup

setup(name="ln.py",
      version="0.2",
      description="symlinks made easier",
      url="https://github.com/dmerejkowsky/ln.py",
      author="Dimitri Merejkowsky",
      author_email="d.merej@gmail.com",
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
