from ckan import model
from ckan.logic import NotAuthorized, NotFound, ValidationError, get_action
from translation import DICTIONARY
import ckan.plugins.toolkit as tk
import pylons.config as config
from ckan.common import _

def init_translation():
    '''
    update dictionary
    '''


    context = {'model': model,
       'session': model.Session,
       'ignore_auth': True}
    
    admin_user = get_action('get_site_user')(context,{})

    context = { 'model': model,
                'session': model.Session,
                'user': admin_user,
                'ignore_auth': True,
                }
    try:
        for record in DICTIONARY:
            show_dict = {
                    'terms': record.get('term'),
                    'lang_codes': record.get('lang_code'),
                    }
            
            trns = get_action('term_translation_show')(context, show_dict)
            if not len(trns):#if not exists, then insert
                update_dict = {
                        'term': record.get('term'),
                        'term_translation': record.get('term_translation'),
                        'lang_code': record.get('lang_code'),
                        }
                result = get_action('term_translation_update')(context, update_dict)

    except NotAuthorized:
        tk.abort(401, _('Not authorized to see this page'))
    except NotFound:
        tk.abort(401, _('There is no registered words for this organization'))#should not turn up
    except ValidationError:
        tk.abort(401, _('Validation Error'))

def translate_dropdown_text(options):
    for option in options:
        if 'text' in option and option.get('text'):
            trns = translate(option.get('text'))
            option.update({'text': trns})
    return options

def translate(term, lang_code=None):

    if not lang_code:
        lang_code = config.get('ckan.locale_default', 'en_AU')

    context = { 'model': model,
                'session': model.Session,
                'user':  tk.c.user or tk.c.author,
                'ignore_auth': True,
                }
    show_dict = {
            'terms': term,
            'lang_codes': lang_code,
            }
    trns = get_action('term_translation_show')(context, show_dict)
    if trns and len(trns):
        record = trns[0]
        return record.get(u'term_translation')
    else:
        return _(term)



