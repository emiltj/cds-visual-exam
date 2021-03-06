<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/emiltj/cds-visual-exam">
    <img src="../README_images/vis_logo.png" alt="Logo" width="200" height="200">
  </a>
  <h2 align="center">Stylized paintings and classification</h2>

  <p align="center">
    Assignment 6
    <br />
    <a href="https://github.com/emiltj/cds-visual-exam/issues">Report Bug</a>
    ·
    <a href="https://github.com/emiltj/cds-visual-exam/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#assignment-description">Assignment description</a></li>
    <li><a href="#methods">Methods</a></li>
    <li><a href="#results-and-discussion">Results and discussion</a></li>
    <li><a href="#usage">Usage</a></li>
          <ul>
        <li><a href="#optional-arguments">Optional arguments</a></li>
      </ul>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ASSIGNMENT DESCRIPTION -->
## Assignment description

This self-assigned assignment has two main questions it seeks to investigate. The investigation is not hypothesis driven nor research oriented. Rather, it is meant to be a fun and atypical way of exploring some methods used in visual analytics.

**Question 1 - Generating stylized paintings**

_Is it possible to use the method of style transfer to stylize paintings of one artist with the style of another?_ 
This assignment seeks to investigate the possibility of not just transferring style from a painting to an actual image as is so often done, but to explore the transferral of the style of one painting to another painting which already is painted in a particular style. Using paintings from the artists _Cezanne_ and _Monet_ from the [impressionist paintings dataset](https://www.kaggle.com/delayedkarma/impressionist-classifier-data), create a script which generates new stylized images. The stylized images should contain the contents of Cezanne with styles of Monet and vice versa.
* Save the stylized images in unique folders with names specifying the which artist the content and style came from.
* Save examples that clearly show the before and after result; save an image which includes content image, style image and the resulting stylized image.

**Question 2 - Classification of stylized images**

_When CNN's classify paintings from artists, do they rely on the style of a given image? Or rather more on the content of the image?_ This part of the assignment seeks to train and test a classifier on the original paintings, and subsequently use the same trained model to classify the stylized paintings. Are Monet paintings with Cezanne style classified as Monet due to their content? Or rather classified as Cezanne due to their style? In other words, investigate the importance of content vs. style when classifying paintings.
* Use a pre-trained CNN classifier to distinguish between Cezanne paintings and Monet paintings.
* Use the same model to classify between the newly generated stylized images. 
* Discuss the findings and consider whether the results tell us something general about either the classifier **or** about the stylization process. 

<!-- METHODS -->
## Methods

**Generating stylized paintings:**

This script utilizes neural style transfer. Style transfer refers to the act of minimizing the distance between two sets of embedded images. One image (the style image) is embedded using the first few layers of a neural network. The other image (the content image) is embedded using the same neural network, but using the first <ins>many</ins> layers of the network. Likewise, the embedded image from this layer is also extracted. Using these two embeddings, style transfer then seeks to synthesize the two with regards to a loss function that minimizes the distance between the content embedding and the style embedding. Sometimes - as in the specific model use here - a Lagrange multiplier is introduced, which determines the weight of importance of the style embedding (level of stylization). 

The original paintings were loaded and their order shuffled. They were then paired by their new shuffled index and each pair was then use to generate two new stylized paintings using the ["magenta/arbitrary-image-stylization-v1-256"](https://arxiv.org/abs/1705.06830) style transfer procedure. Content from painting A and style from painting B (and vice versa) were synthesized into stylized images. The stylized images were then preprocessed and a few examples of content + style + stylized images were saved to the [examples](https://github.com/emiltj/cds-visual-exam/tree/main/assignment_6/out/examples) directory in the directory "out". The entire script is designed to generalize to any other image corpora of any size. The script is furthermore designed so that you may specify both inpaths and outpaths.

<br/>

**Classifying paintings and stylized paintings:**

Both the original paintings and the stylized paintings were loaded using a self-defined function and labels were automatically assigned. The paintings were then resized and formatted, as to match the input expectations of the subsequently defined pre-trained CNN model ([MobileNetV2](https://arxiv.org/abs/1801.04381)). The layers of the models that were not loaded from MobileNetV2 were then trained to classify the artists of the original paintings. Later it was tested on an unseen subset of the same original data. The same model was then set to classify the stylized images. The training history as well as the classification reports for both test sets were printed to the terminal and saved to the [out](https://github.com/emiltj/cds-visual-exam/tree/main/assignment_6/out) directory if specified by the argument --save.

<br/>

**On a more general level (this applies to all assignments):**

I have tried to as accessible and user-friendly as possible. This has been attempted by the use of:
* Smaller functions. These are intended to solve the sub-tasks of the assignment. This is meant to improve readability of the script, as well as simplifying the use of the script.
* Information prints. Information is printed to the terminal to allow the user to know what is being processed in the background
* Argparsing. Arguments that let the user determine the behaviour and paths of the script (see <a href="#optional-arguments">"Optional arguments"</a> section for more information)


<!-- RESULTS AND DISCUSSION -->
## Results and discussion

#### Generating stylized paintings:
<p align="center">
<em>
Top: Content
<br/>
Middle: Style
<br/>
Bottom: Stylized painting
</em>
<br/>
</p>
<p align="center"><a href="https://github.com/emiltj/cds-visual-exam/blob/main/assignment_6/out/examples/example_11.jpg"><img src="./out/examples/example_11.jpg" alt="Logo" width="256" height="768"></a>&nbsp; &nbsp; &nbsp; &nbsp;<a href="https://github.com/emiltj/cds-visual-exam/blob/main/assignment_6/out/examples/example_1.jpg"><img src="./out/examples/example_1.jpg" alt="Logo" width="256" height="768"></a></p>
<p align="center"><em>Content: Cezanne, style: Monet  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Content: Cezanne, style: Monet</em><p/>

When looking at the above two paintings and ([the rest of the examples](https://github.com/emiltj/cds-visual-exam/tree/main/assignment_6/out/examples)), it does indeed seem possible to transfer style from a painting, to another painting which already embodies a style of its own. However, from a brief glance at the 20 examples it seems that in rare instances when using some portraits of people as style image, the process seems to generate paintings that can be hard to interpret (e.g. [painting 12](https://github.com/emiltj/cds-visual-exam/blob/main/assignment_6/out/examples/example_12.jpg)).

Alternatively to the random pairings of style/content images, one could have considered extracting the styles of all paintingss of one artist and then subsequently found the weights resulting in the least information loss across all these style embeddings. This way we would have the general style of an artist to use as the style image when stylizing images. However, a caveat to this method would be the artist we have here, tend to not have the same style of painting over time. Moreover, the fact that the style embedding inevitably also extracts bits of content, would mean that one would have to acquire a very large number of paintings from an artist to model out the noise.

#### Classification of stylized images
  
|           |                    |                    |                    |                    |                    | 
|-----------|--------------------|--------------------|--------------------|--------------------|--------------------| 
|           | monet              | cezanne            | accuracy           | macro avg          | weighted avg       | 
| precision | 0.92 | 0.97  | 0.94 | 0.95 | 0.95 | 
| recall    | 0.97 | 0.92 | 0.94 | 0.94 | 0.94 | 
| f1-score  | 0.95 | 0.94 | 0.94 | 0.94 | 0.94 | 
| support   | 101.0              | 98.0               | 0.94 | 199.0              | 199.0              | 

<em> Original paintings classification report </em>

As can be seen in the classification report when predicting the original paintings, the classifier is able with an macro average F1-score of .94 - in other words performing reasonably well. This was expected, given F1-scores of approx. .32 when classifying between 10 artists in assignment 5.

<br/>
  
|           |                     |                     |                     |                     |                     | 
|-----------|---------------------|---------------------|---------------------|---------------------|---------------------| 
|           | monet               | cezanne             | accuracy            | macro avg           | weighted avg        | 
| precision | 0.21 | 0.28  | 0.25 | 0.24  | 0.24 | 
| recall    | 0.18 | 0.32   | 0.25 | 0.25 | 0.25 | 
| f1-score  | 0.19 | 0.3 | 0.25 | 0.24   | 0.24   | 
| support   | 497.0               | 497.0               | 0.25 | 994.0               | 994.0               | 

<em> Stylized paintings classification report. **NOTE: The Monet paintings with style from Cezanne had - for this classification - their True label set as "Monet".** </em>

From inspecting the classification report when predicting the stylized images, we can see that the classifier predicted roughly 25% of the Monet paintings with Cezanne style, as Monet (and vice versa). 

Can we use this report for shedding light on the question of "_Are Monet paintings with Cezanne style classified as Monet due to their content? Or rather classified as Cezanne due to their style? Discuss the findings and consider whether the results tell us something general about either the classifier or about the stylization process._"

There are two ways of interpreting these results. The first being that the model bases its predictions not so much on the content of the painting, but rather on the style. Style could in other words be interpreted as more important for this classifier. However, a confound comes in the way of going to this conclusion as this would assume that the paintings are 50% content of one artist, and 50% style of one artist. The other way of interpreting the results takes the way in which the stylized paintings were generated into account. The classification results are likely the product of the fact that the stylized paintings that were synthesized were not 50% content and 50% style in the first place. Neural style transfer in its most basic form seeks to minimize the distance between the content of one image and the style of another - resulting in roughly half of each. However, the ["magenta/arbitrary-image-stylization-v1-256"](https://arxiv.org/abs/1705.06830) model uses a more sophisticated approach and from looking at their paper, they seem not to have reported the level of stylization that their model uses (Lagrange multiplier, determining the relative strength of the style loss).

In summary, the classification report of the stylized paintings cannot lead to any direct conclusions when it comes to how CNN's work in general. If instead a simple neural transfer model that stylized images with equal weighting to both content and style had been used, then we would perhaps have been able to make some inferences about the relative importance that content and style had on the classifier. If anything was to be said about the results it would be that they suggest that the neural style transfer method used here, might synthesize stylized images using a lot of information from the style image. 

<!-- USAGE -->
## Usage

Make sure to follow the instructions in the README.md located at the parent level of this repository, for the required installation of the virtual environment as well as the data download.

Subsequently, use the following code (when within the ```cds-visual-exam``` folder):

```bash
cd assignment_6
source ../cv101/bin/activate # If not already activated
python generate_stylized.py
python cnn_stylized.py
```

### Optional arguments:
generate_stylized.py arguments for commandline to consider:
-       "-i",
        "--inpatha", 
        type = str,
        default = os.path.join("data", "content_cezanne_style_cezanne", "*.jpg"), # Default path to corpus, when none is specified
        required = False,
        help= "str - path to image corpus a")
        
-       "-I",
        "--inpathb",
        type = str,
        default = os.path.join("data", "content_monet_style_monet", "*.jpg"), # Default path to corpus, when none is specified
        required = False,
        help= "str - path to image corpus b")      
-       "-o",
        "--outpatha",
        type = str,
        default = os.path.join("data", "content_cezanne_style_monet"), # Default path to corpus, when none is specified
        required = False,
        help= "str - path to output path of the stylized images with content_a_style_b")
-       "-O",
        "--outpathb",
        type = str,
        default = os.path.join("data", "content_monet_style_cezanne"), # Default path to corpus, when none is specified
        required = False,
        help= "str - path to output path of the stylized images with content_b_style_a")        
        
cnn_stylized.py arguments for commandline to consider:
-       "-d",
        "--datapath",
        type = str,
        default = "data", # Default when not specifying name of outputfile
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "str - containing folderpath to parent data folder.")
-       "-e",
        "--epochs", 
        type = int,
        default = 10, # Default when not specifying anything in the terminal
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "int - specifying number of epochs for re-training the trainable layers of the cnn.")
-       "-s",
        "--save", 
        type = bool,
        default = True, # Default when not specifying anything else
        required = False, # Since we have a default value, it is not required to specify this argument
        help = "bool - specifying whether to save classification reports")

<!-- CONTACT -->
## Contact

Feel free to write me, Emil Jessen for any questions.
You can do so on [Slack](https://app.slack.com/client/T01908QBS9X/D01A1LFRDE0) or on [Facebook](https://www.facebook.com/emil.t.jessen/).
