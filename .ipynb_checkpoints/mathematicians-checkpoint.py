{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "1+2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'beautifulsoup4' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-2-4a4c632b2d60>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m print(beautifulsoup4.__version__\n\u001b[0m\u001b[1;32m      2\u001b[0m      )\n",
      "\u001b[0;31mNameError\u001b[0m: name 'beautifulsoup4' is not defined"
     ]
    }
   ],
   "source": [
    "print(beautifulsoup4.__version__\n",
    "     )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "cannot import name 'beautifulsoup4' from 'bs4' (/anaconda3/lib/python3.7/site-packages/bs4/__init__.py)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-3-318cfa008b5e>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mbs4\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mbeautifulsoup4\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mImportError\u001b[0m: cannot import name 'beautifulsoup4' from 'bs4' (/anaconda3/lib/python3.7/site-packages/bs4/__init__.py)"
     ]
    }
   ],
   "source": [
    "from bs4 import beautifulsoup4\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "from requests import get "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-1-191aa2638544>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-1-191aa2638544>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    pip3 install mathematicians\u001b[0m\n\u001b[0m               ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "pip3 install mathematicians\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from requests.exceptions import RequestException"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from contextlib import closing \n",
    "def simple_get():\n",
    "    try:\n",
    "        with closing(get(url, stream=True)) as resp:\n",
    "            if is_good_response(resp):\n",
    "                return resp.content\n",
    "            else:\n",
    "                return None\n",
    "        \n",
    "    except RequestException as e:\n",
    "        log_error('Error during requests to {0} : {1}'.format(url, str(e)))\n",
    "        return None\n",
    "def is_good_response(resp):\n",
    "    content_type = resp.headers['Content-Type'].lower()\n",
    "    return (resp.status_code == 200\n",
    "            and content_type is not None\n",
    "            and content_type.find('html') > -1)\n",
    "\n",
    "def log_error(e):\n",
    "    print(e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
