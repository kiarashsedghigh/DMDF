# (Double the Mark, Double the Defense (DMDF))
The development of Artificial General Intelligence (AGI) is driven by Large Language Models (LLMs), which excel in tasks like translation, dialogue, and code generation. However, this also exposes them to misuse, including misinformation and model extraction attacks. Despite advances in the design of robust watermarks, recent attacks have not yet been tested against these newer schemes, raising concerns about their effectiveness for practical use.

This work investigates whether dual watermarks enhance a model’s robustness against the Watermark Stealing method, a novel technique that strengthens scrubbing attacks. We assess the effectiveness of this approach and analyze if employing two watermarks can effectively
counter its impact. Our findings will clarify whether existing single watermark schemes are suitable for real-world deployment or if a transition to dual watermarks is necessary.


## Hardware, Software, and Dataset
To access GPU hardware, we used GPU Cloud Infrustracture provided by
[Lambda](https://lambdalabs.com/?matchtype=p&adgroup=167368709642&feeditemid=&loc_interest_ms=&loc_physical_ms=9052965&network=g&device=c&devicemodel=&adposition=&utm_source=google&utm_campaign=Google_Search_Cloud-Brand&utm_medium=search&utm_term=lambda%20labs&utm_content=708570750692&hsa_acc=1731978716&hsa_cam=17699749392&hsa_grp=167368709642&hsa_ad=708570750692&hsa_src=g&hsa_tgt=kwd-315332575824&hsa_kw=lambda%20labs&hsa_mt=p&hsa_net=adwords&hsa_ver=3&gad_source=1&gbraid=0AAAAADrJiRyFjrjMIzf2DlNVlC_vpYQY1&gclid=CjwKCAiArva5BhBiEiwA-oTnXQzMM4cO6MmYZwb_e4GvKiKsaeQ4sobwCciPl6y80CTyoG7cjNw9KBoCdFgQAvD_BwE) group.
Resources have been as follows:

- _Hardware_: A100 (40GB SXM4, 30 CPU Core, 214GB RAM)
- _Programming_: Python3 (3.10.12)
- _Dataset_: [C4](https://arxiv.org/pdf/1910.10683)



## Python Virtual Environment
After cloning this repository, creating a Python3 virtual environment
to install the required dependencies is highly recommended

```
$ python3 -m venv ENV_NAME
```

Further, you can activate the environment as follows:
```
$ source ./ENV_NAME/bin/activate
```



## Building and Dependencies 
For each project, whether it is Watermark Stealing or Dual Watermark, 
first clone their project:

```
$ git clone https://github.com/eth-sri/watermark-stealing.git
```

```
$ git clone https://github.com/chaoyitud/Dual-Watermarks.git
```

Then navigate to the corresponding directory using cd and run either `bash 
install.sh` or `bash setup.sh`, as specified for the project.
This will install all the necessary packages for the respective project. 
However, some packages might not be installed due to assumptions in the 
setup scripts. Below are the most likely missing packages that may not already exist on your 
system:


```
$ pip3 install dataset scipy transformers \
sentencepiece sacremoses json5 nltk matplotlib \
gradio dill decite dahuffman hash_cpp xxhash argostranslate lingua
```


