from setuptools import setup, find_packages

setup(
    name="xibra_v",  # اسم مكتبتك
    version="0.1",  # الإصدار الأول
    packages=find_packages(),
    install_requires=[
        'pyfiglet',
        'colorama',
        'twine',
        'setuptools',
        'wheel'
    ],  # أضف المكتبات التي تعتمد عليها هنا
    author="ibra1410",  # اسم المؤلف
    author_email="ibraus34@gmail.com",  # بريدك الإلكتروني
    description="A simple encryption library",
    long_description=open("README.md").read(),  # وصف المكتبة الكامل
    long_description_content_type="text/markdown",  # نوع المحتوى
    url="https://github.com/ibra1410/xibra_v",  # رابط المستودع على GitHub
    classifiers=[  # التصنيفات الخاصة بمكتبتك على PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
