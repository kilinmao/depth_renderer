import os
import shutil

rename_view_dict = {
'001':'060',
'002':'052',
'003':'051',
'004':'050',
'005':'042',
'006':'041',
'007':'040',
'008':'032',
'009':'031',
'010':'030',
'011':'022',
'012':'021',
'013':'020',
'014':'012',
'015':'011',
'016':'010',
'017':'002',
'018':'001',
'019':'000',
'020':'072',
'021':'071',
'022':'070',
'023':'062',
'024':'061',
'025':'360',
'026':'352',
'027':'351',
'028':'350',
'029':'342',
'030':'341',
'031':'340',
'032':'332',
'033':'331',
'034':'330',
'035':'322',
'036':'321',
'037':'320',
'038':'312',
'039':'311',
'040':'310',
'041':'302',
'042':'301',
'043':'300',
'044':'372',
'045':'371',
'046':'370',
'047':'362',
'048':'361',
'049':'460',
'050':'452',
'051':'451',
'052':'450',
'053':'442',
'054':'441',
'055':'440',
'056':'432',
'057':'431',
'058':'430',
'059':'422',
'060':'421',
'061':'420',
'062':'412',
'063':'411',
'064':'410',
'065':'402',
'066':'401',
'067':'400',
'068':'472',
'069':'471',
'070':'470',
'071':'462',
'072':'461',
'073':'260',
'074':'252',
'075':'251',
'076':'250',
'077':'242',
'078':'241',
'079':'240',
'080':'232',
'081':'231',
'082':'230',
'083':'222',
'084':'221',
'085':'220',
'086':'212',
'087':'211',
'088':'210',
'089':'202',
'090':'201',
'091':'200',
'092':'272',
'093':'271',
'094':'270',
'095':'262',
'096':'261'
}

view_list = [
    'view060',
    'view052',
    'view051',
    'view050',
    'view042',
    'view041',
    'view040',
    'view032',
    'view031',
    'view030',
    'view022',
    'view021',
    'view020',
    'view012',
    'view011',
    'view010',
    'view002',
    'view001',
    'view000',
    'view072',
    'view071',
    'view070',
    'view062',
    'view061',
    'view360',
    'view352',
    'view351',
    'view350',
    'view342',
    'view341',
    'view340',
    'view332',
    'view331',
    'view330',
    'view322',
    'view321',
    'view320',
    'view312',
    'view311',
    'view310',
    'view302',
    'view301',
    'view300',
    'view372',
    'view371',
    'view370',
    'view362',
    'view361',
    'view460',
    'view452',
    'view451',
    'view450',
    'view442',
    'view441',
    'view440',
    'view432',
    'view431',
    'view430',
    'view422',
    'view421',
    'view420',
    'view412',
    'view411',
    'view410',
    'view402',
    'view401',
    'view400',
    'view472',
    'view471',
    'view470',
    'view462',
    'view461',
    'view260',
    'view252',
    'view251',
    'view250',
    'view242',
    'view241',
    'view240',
    'view232',
    'view231',
    'view230',
    'view222',
    'view221',
    'view220',
    'view212',
    'view211',
    'view210',
    'view202',
    'view201',
    'view200',
    'view272',
    'view271',
    'view270',
    'view262',
    'view261'
]


rename_model_dict = {}
used_model_list = []

catagery = 'table'

if catagery == 'table':
    path = './datasets/ShapeNetRenderings/04379243'
    all_model_path = './datasets/ShapeNetCore.v2_normalized/04379243'
    not_used_model_path = './datasets/ShapeNetCore.v2_normalized/04379243_not_used'
    rendered_model_path = './datasets/ShapeNetCore.v2_normalized/04379243_rendered'
elif catagery == 'chair':
    all_model_path = './datasets/ShapeNetCore.v2/03001627'
    not_used_model_path = './datasets/ShapeNetCore.v2/03001627_not_used'

def create_name_dict():
    with open(catagery+'.txt','r+') as f:
        items = f.readlines()
        for item in items:
            old = item.split(' ')[0].split('/')[8]
            used_model_list.append(old)
            new = item.split(' ')[1].split('_')[1].split('.')[0]
            rename_model_dict[old] = new
    # print(rename_model_dict)

ids = []
def get_id():
    with open(catagery+'_i.txt','r+') as f:
        items = f.readlines()
        for item in items:
            id = rename_model_dict.get(item.strip('\n'))
            if id != None:
                ids.append(id)
    print(ids)




def get_used_model():
    with open(catagery+'_used.txt','r+') as f:
        items = f.readlines()
        for item in items:
            new = item[0:-12]
            used_model_list.append(new)
    # print(used_model_list)

def select_used_model():
    with os.scandir(all_model_path) as items:
        for item in items:
            if item.is_dir() and rename_model_dict.get(item.name) not in used_model_list:
                shutil.move(all_model_path+'/'+item.name,not_used_model_path)

rendered_model_list = []
def get_rendered_model():
    with os.scandir('datasets/ShapeNetRenderings/04379243') as items:
        for item in items:
            if item.is_dir():
                rendered_model_list.append(item.name)
    with os.scandir('datasets/ShapeNetCore.v2_normalized/04379243') as items:
        for item in items:
            if item.is_dir() and (item.name in rendered_model_list):
                shutil.move(all_model_path+'/'+item.name,rendered_model_path)


def rename():
    with os.scandir(path) as items:
        for item in items:
            if item.is_dir():
                with os.scandir(path+'/'+item.name) as imgs:
                    for img in imgs:
                        if os.path.splitext(img.name)[1] == '.png':
                            model_name = rename_model_dict[item.name]
                            view_name = rename_view_dict[img.name[-7:-4]]
                            os.rename(path+'/'+item.name+'/'+img.name,path+'/'+item.name+'/'+model_name+'_view'+view_name+'.png')

def convert_path():

    # os.chdir(path+'_')
    # for view in view_list:
    #     os.mkdir(view)

    with os.scandir(path) as entries:
        os.chdir(path)
        for entry in entries:
            if entry.is_dir():
                with os.scandir(entry.name) as directory:
                    for img in directory:
                        if os.path.splitext(img)[1] == '.png':
                            dir_name = img.name[-11:-4]
                            print('../04379243_/'+dir_name+'/'+img.name)
                            shutil.copyfile(entry.name+'/'+img.name,'../04379243_/'+dir_name+'/'+img.name)
    print('finish')





if __name__ == '__main__':
    create_name_dict()
    get_id()
    # get_used_model()
    # select_used_model()
    # rename()
    # get_rendered_model()
    # convert_path()
