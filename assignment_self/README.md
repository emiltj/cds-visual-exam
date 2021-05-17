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
This assignment seeks to investigate the possibility of not just transferring style from a painting to an actual image as is so often done, but to explore the transferral of the style of one painting to another painting. Using paintings from the artists _Cezanne_ and _Monet_ from the [impressionist paintings dataset](https://www.kaggle.com/delayedkarma/impressionist-classifier-data), create a script which generates new stylized images. The stylized images should contain the contents of Cezanne with styles of Monet and vice versa.
* Save the stylized images in unique folders with names specifying the stylized images.
* Save examples that clearly show the before and after result; save an image which includes content image, style image and the resulting stylized image.

**Question 2 - Classification of stylized images**

_When CNN's classify paintings from artists, do they rely on the style of a given image? Or rather more on the content of the image?_ This part of the assignment seeks to train and test a classifier on the original paintings, and subsequently use the same trained model to classify the stylized paintings. In other words, investigate the importance of content vs. style when classifying paintings.
* Use a pre-trained CNN classifier to distinguish between Cezanne paintings and Monet paintings.
* Use the same model to classify between the newly generated stylized images. 
* Are Monet paintings with Cezanne style classified as Monet due to their content? Or rather classified as Cezanne due to their style? Discuss the findings and consider whether the results tell us something general about either the classifier or about the stylization process. 

<!-- METHODS -->
## Methods

**Generating stylized paintings**

The original paintings were loaded and their order shuffled. They were then paired by index and each pair was then use to generate two new stylized paintings using the ["magenta/arbitrary-image-stylization-v1-256"](https://arxiv.org/abs/1705.06830). Content from painting A and style from painting B and vice versa. The stylized images were then preprocessed and a few examples of content + style + stylized images were saved to the ```./out/``` folder. The entire script is designed to generalize to any other image corpora of any size.

**Classifying paintings and stylized paintings**

Both the original paintings and the stylized paintings were loaded using a self-define function and labels were automatically assigned. The paintings were then resized and formatted, as to match the input expectations of the subsequently defined pre-trained CNN model ([MobileNetV2](https://arxiv.org/abs/1801.04381)). The model was then trained to classify the artists of the original paintings, and later tested on an unseen subset of the same data. The same model was then set to classify the stylized images. The training history as well as the classification reports for both test sets were printed to the terminal and saved to the ```./out/``` folder.

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
Bottom: Stylized image
</em>
<br/>
</p>
<p align="center"><a href="https://github.com/emiltj/cds-visual-exam/blob/main/assignment_self/out/example_7.jpg"><img src="./out/example_11.jpg" alt="Logo" width="256" height="768"></a>&nbsp; &nbsp; &nbsp; &nbsp;<a href="https://github.com/emiltj/cds-visual-exam/blob/main/assignment_self/out/example_17.jpg"><img src="./out/example_1.jpg" alt="Logo" width="256" height="768"></a></p>
<p align="center"><em>Content: Monet, style: Cezanne  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Content: Gauguin, style: Cezanne</em><p/>

When looking at the above two images and ([the rest of the examples](https://github.com/emiltj/cds-visual-exam/tree/main/assignment_self/out)), it does indeed seem possible to transfer style from a painting, to another painting. However, from a brief glance at the 20 examples it seems that when using portraits of people as style image, the process seems to generate paintings that are hard to interpret (e.g. [image 12](https://github.com/emiltj/cds-visual-exam/blob/main/assignment_self/out/example_12.jpg).

Alternatively to the random pairings of style/content images, one could have considered extracting the styles of all images of one artist and then subsequently found the weights resulting in the least information loss across all these images. This way we would have the general style of an artist to use as the style image when stylizing images. However, a caveat to this method would be the artist we have here, tend to not have the same style of painting over time. The fact that the noise from the content that is inevitably fed into the style imbedding would also require an enormous number of paintings from each artist.

#### Classification of stylized images
<p align="center">
  
|           |                    |                    |                    |                    |                    | 
|-----------|--------------------|--------------------|--------------------|--------------------|--------------------| 
|           | monet              | cezanne            | accuracy           | macro avg          | weighted avg       | 
| precision | 0.92 | 0.97  | 0.94 | 0.95 | 0.95 | 
| recall    | 0.97 | 0.92 | 0.94 | 0.94 | 0.94 | 
| f1-score  | 0.95 | 0.94 | 0.94 | 0.94 | 0.94 | 
| support   | 101.0              | 98.0               | 0.94 | 199.0              | 199.0              | 

<em> Original paintings classification report </em></p>

<br/>

<p align="center">
  
|           |                     |                     |                     |                     |                     | 
|-----------|---------------------|---------------------|---------------------|---------------------|---------------------| 
|           | monet               | cezanne             | accuracy            | macro avg           | weighted avg        | 
| precision | 0.21 | 0.28  | 0.25 | 0.24  | 0.24 | 
| recall    | 0.18 | 0.32   | 0.25 | 0.25 | 0.25 | 
| f1-score  | 0.19 | 0.3 | 0.25 | 0.24   | 0.24   | 
| support   | 497.0               | 497.0               | 0.25 | 994.0               | 994.0               | 

<em> Stylized paintings classification report </em></p>

As can be seen in the classification report when predicting the original paintings (top)

As can be seen in the classification report when predicting the stylized images (bottom)

https://en.wikipedia.org/wiki/Neural_Style_Transfer#Formulation

Style transfer refers to the act of minimizing the loss of information between two sets of embedded images. One image (the style image) is embedded using the first few layers of a neural network and network activations are sampled from this embedded image. The other image (the content image) is embedded using the same neural network, but using the first <ins>many</ins> layers of the network. Likewise, the embedded image from this layer is also extracted. Using these two embeddings, style transfer then seeks to synthesize the two with regards to a loss function that minimizes the information loss of both images.

<!-- USAGE -->
## Usage

Make sure to follow the instructions in the README.md located at the parent level of this repository, for the required installation of the virtual environment as well as the data download.
Subsequently, use the following code:

```bash
cd cds-visual/assignment_2
source ../cv101/bin/activate
python generate_stylized.py
python cnn_stylized.py
```

### Optional arguments:
s
generate_stylized.py arguments for commandline to consider:
-       s
-       
cnn_stylized.py arguments for commandline to consider:
-       

<!-- CONTACT -->
## Contact

Feel free to write me, Emil Jessen for any questions.
You can do so on [Slack](https://app.slack.com/client/T01908QBS9X/D01A1LFRDE0) or on [Facebook](https://www.facebook.com/emil.t.jessen/).
