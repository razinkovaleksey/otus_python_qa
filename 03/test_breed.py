import json
import mimetypes
import requests
import pytest



def is_url_image(url):
    mimetype, encoding = mimetypes.guess_type(url)
    return mimetype and mimetype.startswith('image')


def test_list_all_status_code():
    """Assert integer addition"""
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    assert response.status_code == 200


def test_list_all_status_success():
    """Assert integer addition"""
    response_text = requests.get('https://dog.ceo/api/breeds/list/all').text
    response_json = json.loads(response_text)
    assert response_json['status'] == 'success'


def test_assert_spaniel_info():
    response_text = requests.get('https://dog.ceo/api/breed/spaniel').text
    response_json = json.loads(response_text)
    assert response_json['message']['info'] == "A spaniel is a type of gun dog. Spaniels were especially bred to flush game out of denser brush. By the late 17th century spaniels had been specialized into water and land breeds."
    assert response_json['message']['name'] == 'Spaniel'


def test_assert_random_breed_image():
    response_text = requests.get('https://dog.ceo/api/breeds/image/random').text
    response_json = json.loads(response_text)
    image_url = response_json['message']
    assert is_url_image(image_url)


@pytest.mark.parametrize('breed', ('borzoi', 'boxer', 'affenpinscher'))
def test_random_image_by_breed(breed):
    response_text = requests.get('https://dog.ceo/api/breed/{breed}/images/random'.format(breed=breed)).text
    response_json = json.loads(response_text)
    image_url = response_json['message']
    assert is_url_image(image_url)


@pytest.mark.parametrize('subbreed', ('chesapeake', 'curly', 'flatcoated', 'golden'))
def test_random_image_by_sub_breed(subbreed):
    response_text = requests.get(
        'https://dog.ceo/api/breed/retriever/{subbreed}/images/random'.format(subbreed=subbreed)).text
    response_json = json.loads(response_text)
    image_url = response_json['message']
    assert is_url_image(image_url)


breeds_dict = {"affenpinscher": [], "african": [], "airedale": [], "akita": [], "appenzeller": [], "basenji": [],
               "beagle": [], "bluetick": [], "borzoi": [], "bouvier": [], "boxer": [], "brabancon": [], "briard": [],
               "buhund": ["norwegian"], "bulldog": ["boston", "english", "french"], "bullterrier": ["staffordshire"],
               "cairn": [], "cattledog": ["australian"], "chihuahua": [], "chow": [], "clumber": [], "cockapoo": [],
               "collie": ["border"], "coonhound": [], "corgi": ["cardigan"], "cotondetulear": [], "dachshund": [],
               "dalmatian": [], "dane": ["great"], "deerhound": ["scottish"], "dhole": [], "dingo": [], "doberman": [],
               "elkhound": ["norwegian"], "entlebucher": [], "eskimo": [], "frise": ["bichon"], "germanshepherd": [],
               "greyhound": ["italian"], "groenendael": [],
               "hound": ["afghan", "basset", "blood", "english", "ibizan", "walker"], "husky": [], "keeshond": [],
               "kelpie": [], "komondor": [], "kuvasz": [], "labrador": [], "leonberg": [], "lhasa": [], "malamute": [],
               "malinois": [], "maltese": [], "mastiff": ["bull", "english", "tibetan"], "mexicanhairless": [],
               "mix": [], "mountain": ["bernese", "swiss"], "newfoundland": [], "otterhound": [], "papillon": [],
               "pekinese": [], "pembroke": [], "pinscher": ["miniature"], "pointer": ["german", "germanlonghair"],
               "pomeranian": [], "poodle": ["miniature", "standard", "toy"], "pug": [], "puggle": [], "pyrenees": [],
               "redbone": [], "retriever": ["chesapeake", "curly", "flatcoated", "golden"], "ridgeback": ["rhodesian"],
               "rottweiler": [], "saluki": [], "samoyed": [], "schipperke": [], "schnauzer": ["giant", "miniature"],
               "setter": ["english", "gordon", "irish"], "sheepdog": ["english", "shetland"], "shiba": [],
               "shihtzu": [], "spaniel": ["blenheim", "brittany", "cocker", "irish", "japanese", "sussex", "welsh"],
               "springer": ["english"], "stbernard": [],
               "terrier": ["american", "australian", "bedlington", "border", "dandie", "fox", "irish", "kerryblue",
                           "lakeland", "norfolk", "norwich", "patterdale", "russell", "scottish", "sealyham", "silky",
                           "tibetan", "toy", "westhighland", "wheaten", "yorkshire"], "vizsla": [],
               "waterdog": ["spanish"], "weimaraner": [], "whippet": [], "wolfhound": ["irish"]}

breeds_only_with_subbreed = {key: value for (key, value) in breeds_dict.items() if value}
breed_subbread_set = ((breed, subbreed) for breed in breeds_only_with_subbreed for subbreed in
                      breeds_only_with_subbreed[breed])


@pytest.mark.parametrize('breed,subbread', breed_subbread_set)
def test_random_image_by_breed_and_subbread(breed, subbread):
    response_text = requests.get(
        'https://dog.ceo/api/breed/{breed}/{subbread}/images/random'.format(breed=breed, subbread=subbread)).text
    response_json = json.loads(response_text)
    image_url = response_json['message']
    assert is_url_image(image_url)
