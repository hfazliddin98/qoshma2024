import csv
import xlwt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Arizalar


@csrf_exempt
def ariza_yuborish(request):
    data = ''
    if request.method == 'POST':
        familiya = request.POST['familiya']
        ism = request.POST['ism']
        sharif = request.POST['sharif']
        telefon = request.POST['telefon']
        pasport_serya = request.POST['pasport_serya']  
        pasport_raqam = request.POST['pasport_raqam']
        jshr = request.POST['jshr']
        pasport_rasm = request.FILES['pasport_rasm'] 
        natariyus_pasport = request.FILES['natariyus_pasport'] 
        daraja = request.POST['daraja']      
        yonalish = request.POST['yonalish']
        diplom_serya_raqam = request.POST['diplom_serya_raqam']
        diplom_rasm = request.FILES['diplom_rasm']
        natariyus_diplom = request.FILES['natariyus_diplom']
        bitirgan_yil = request.POST['bitirgan_yil']
        bitirgan_muassasa = request.POST['bitirgan_muassasa']
        viloyat = request.POST['viloyat']
        tuman = request.POST['tuman']
        kocha = request.POST['kocha']
        rozilik = request.POST['rozilik']
        print(rozilik)
        if rozilik == 'True':           
            rozilik_bildirish = 'Malumotlarimdan foydalanishga roziman'       
        else:          
            rozilik_bildirish = 'Malumotlarimdan foydalanishga roziman'           
        
        
        if Arizalar.objects.filter(jshr=jshr):
            data = 'Bu foydalanuvchi ariza yuborgan'
        else:
            ariza = Arizalar.objects.create(               
                familiya = familiya, ism = ism, sharif=sharif, 
                telefon = telefon, pasport_serya=pasport_serya,
                pasport_raqam = pasport_raqam, jshr=jshr,
                pasport_rasm=pasport_rasm, daraja=daraja, 
                natariyus_pasport=natariyus_pasport,  
                yonalish=yonalish, diplom_serya_raqam=diplom_serya_raqam,
                diplom_rasm=diplom_rasm,bitirgan_yil=bitirgan_yil,
                natariyus_diplom=natariyus_diplom,
                bitirgan_muassasa=bitirgan_muassasa,viloyat=viloyat,
                tuman=tuman,kocha=kocha,rozilik=rozilik_bildirish               
            ) 
            ariza.save()          
            return redirect('/arizalar/qabul_qilindi/')   
    contex = {
        'data':data,
    }    
    return render(request, 'arizalar/ariza_yuborish.html', contex)



@csrf_exempt
def qabul(request):
    
    contex = {
        
    }
    return render(request, 'arizalar/qabul.html', contex)



@csrf_exempt
def qabul_qilindi(request):
    
    contex = {
        
    }
    return render(request, 'arizalar/qabul_qilindi.html', contex)


@csrf_exempt
def bakalavr(request):
    data = Arizalar.objects.filter(daraja='Bakalavr')
    
    contex = {
      'data':data,  
    }
    return render(request, 'arizalar/bakalavr.html', contex)

@csrf_exempt
def magistr(request):
    data = Arizalar.objects.filter(daraja='Magistratura')
    
    contex = {
       'data':data, 
    }
    return render(request, 'arizalar/magistr.html', contex)

@csrf_exempt
def malumot(request, pk):
    data = Arizalar.objects.filter(id=pk)
    
    contex = {
        'data':data,
    }
    return render(request, 'arizalar/malumot.html', contex)



@csrf_exempt
def bakalavr_csv(request):
        response = HttpResponse(content_type='application/ms-excel')

        response['Content-Disposition'] = 'attachment; filename="arizalar.xls"'

        wb = xlwt.Workbook(encoding='utf-8')

        ws = wb.add_sheet("sheet1")

        row_num = 0

        font_style = xlwt.XFStyle()

        font_style.font.bold = True

        columns = [
            'PNFL',
            'SERIYA', 
            'RAQAM',
            'FAMILYA',
            'ISM',
            'SHARIIFI',
            'YO`NALISH',
            'Attestat (diplom) seriya va raqam',
            'Bitirgan ta`lim muassasasi nomi',
            'Bitirgan yili',  
            'Telefon raqami',
            'Yashash manzili',                           
        ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        talabalar  = Arizalar.objects.filter(daraja='Bakalavr')
        if talabalar:
            for my_row in talabalar: 
                manzil = f'{my_row.viloyat} {my_row.tuman} {my_row.kocha}'                
                row_num = row_num + 1
                ws.write(row_num, 0, my_row.jshr, font_style)
                ws.write(row_num, 1, my_row.pasport_serya, font_style)
                ws.write(row_num, 2, my_row.pasport_raqam, font_style)
                ws.write(row_num, 3, my_row.familiya, font_style)
                ws.write(row_num, 4, my_row.ism, font_style)
                ws.write(row_num, 5, my_row.sharif, font_style)
                ws.write(row_num, 6, my_row.yonalish, font_style)
                ws.write(row_num, 7, my_row.diplom_serya_raqam, font_style)
                ws.write(row_num, 8, my_row.bitirgan_muassasa, font_style)
                ws.write(row_num, 9, my_row.bitirgan_yil, font_style)
                ws.write(row_num, 10, my_row.telefon, font_style)
                ws.write(row_num, 11, manzil, font_style)
                                   

            wb.save(response)
            return response
        else:
            return redirect('/')
    






@csrf_exempt
def magistr_csv(request):
        response = HttpResponse(content_type='application/ms-excel')

        response['Content-Disposition'] = 'attachment; filename="arizalar.xls"'

        wb = xlwt.Workbook(encoding='utf-8')

        ws = wb.add_sheet("sheet1")

        row_num = 0

        font_style = xlwt.XFStyle()
        
        font_style.font.bold = True

        columns = [
            'PNFL',
            'SERIYA', 
            'RAQAM',
            'FAMILYA',
            'ISM',
            'SHARIIFI',
            'YO`NALISH',
            'Attestat (diplom) seriya va raqam',
            'Bitirgan ta`lim muassasasi nomi',
            'Bitirgan yili',  
            'Telefon raqami',
            'Yashash manzili',                           
        ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        talabalar  = Arizalar.objects.filter(daraja='Magistratura')
        if talabalar:
            for my_row in talabalar: 
                manzil = f'{my_row.viloyat} {my_row.tuman} {my_row.kocha}'                
                row_num = row_num + 1
                ws.write(row_num, 0, my_row.jshr, font_style)
                ws.write(row_num, 1, my_row.pasport_serya, font_style)
                ws.write(row_num, 2, my_row.pasport_raqam, font_style)
                ws.write(row_num, 3, my_row.familiya, font_style)
                ws.write(row_num, 4, my_row.ism, font_style)
                ws.write(row_num, 5, my_row.sharif, font_style)
                ws.write(row_num, 6, my_row.yonalish, font_style)
                ws.write(row_num, 7, my_row.diplom_serya_raqam, font_style)
                ws.write(row_num, 8, my_row.bitirgan_muassasa, font_style)
                ws.write(row_num, 9, my_row.bitirgan_yil, font_style)
                ws.write(row_num, 10, my_row.telefon, font_style)
                ws.write(row_num, 11, manzil, font_style)
                                   

            wb.save(response)
            return response
        else:
            return redirect('/')
     
    