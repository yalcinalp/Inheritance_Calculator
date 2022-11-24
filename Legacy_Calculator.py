
def inheritance(lst):

	might_have_duplicate = inheritance_help(lst)
	stack = []
	just_isimler = []

	for kisi in might_have_duplicate:

		if stack == []:
			stack.append(kisi)
			just_isimler.append(kisi[0])

		else:

			if kisi[0] in just_isimler:
				for i in range(len(stack)):
					if stack[i][0] == kisi[0]:

						lst_hal = [stack[i][0], stack[i][1]]
						lst_hal[1] = stack[i][1] + kisi[1]
						stack[i] = (stack[i][0], lst_hal[1])

			else:

				stack.append(kisi)
				just_isimler.append(kisi[0])
	
	return stack	


def pg1(olen_birey, lst, rakam):

	for kisi in lst:
		if kisi[0] == olen_birey:

			mirascının_ismi = kisi[0]

			if type(kisi[-1]) == float or type(kisi[-1]) == int:
				miras_para = kisi[-1]

			else:
				miras_para = rakam 

			partner = kisi[3] 				#direct string
			partner_hayatta_mı = []
			
			for insan in lst:
				if insan[0] == partner:
					if "not dead" in insan:
						partner_hayatta_mı.append(insan[0])

					elif "DEPARTED" in insan:
					
						pass

			if partner_hayatta_mı != []:
			
				#partner hayattadır

				partner_hayatta_mı[0] = (partner,miras_para/4)
				miras_para = (3/4)*miras_para


			elif partner_hayatta_mı == []:

				pass	

			cocuklar = kisi[4]
			canli_cocuks = []
			cansız_fakat_alt_soylu_cocuks = []

			for cocuk in cocuklar:
				for birey in lst:

					if cocuk == birey[0]:
						if "not dead" in birey:
							canli_cocuks.append(cocuk)

						elif "DEPARTED" in birey:
						
								varsa_canlı_alt_soy_listesi = canlı_alt_soy_var_mi(birey[0], lst)

								if varsa_canlı_alt_soy_listesi != []:

									cansız_fakat_alt_soylu_cocuks.append(birey[0])

								elif varsa_canlı_alt_soy_listesi == []:
								
									pass

			birlesmis_birinci_derece_mirasci_cocuklar = canli_cocuks + cansız_fakat_alt_soylu_cocuks


			temporary_mirası_paylasacak_kisi_sayısı = len(birlesmis_birinci_derece_mirasci_cocuklar)


			kisi_bası_dusen_pay = miras_para/temporary_mirası_paylasacak_kisi_sayısı

			temporary_result_1 = []

			for mirascı_birey in canli_cocuks:

				temp_val_1 = (mirascı_birey, kisi_bası_dusen_pay)

				temporary_result_1.append(temp_val_1)

			bos_lst = []	

			for mirascı_birey2 in cansız_fakat_alt_soylu_cocuks:

				#bos_lst.append(pg1(mirascı_birey2, lst, kisi_bası_dusen_pay))

				bos_lst = bos_lst + partnere_para_vermeyen_pg1(mirascı_birey2, lst, kisi_bası_dusen_pay)

			result = bos_lst + temporary_result_1


			if partner_hayatta_mı != []:

				son_result = partner_hayatta_mı + result

				return son_result

			elif partner_hayatta_mı == []:
			
				return result	



def partnere_para_vermeyen_pg1(olen_birey, lst, rakam):  

	for kisi in lst:

		if kisi[0] == olen_birey:

			mirascının_ismi = kisi[0]

			if type(kisi[-1]) == float or type(kisi[-1]) == int:

				miras_para = kisi[-1]

			else:
			
				miras_para = rakam 

			cocuklar = kisi[4]

			canli_cocuks = []

			cansız_fakat_alt_soylu_cocuks = []

			for cocuk in cocuklar:

				for birey in lst:

					if cocuk == birey[0]:

						if "not dead" in birey:

							canli_cocuks.append(cocuk)

						elif "DEPARTED" in birey:
						
								varsa_canlı_alt_soy_listesi = canlı_alt_soy_var_mi(birey[0], lst)

								if varsa_canlı_alt_soy_listesi != []:

									cansız_fakat_alt_soylu_cocuks.append(birey[0])

								elif varsa_canlı_alt_soy_listesi == []:
								
									pass


			birlesmis_birinci_derece_mirasci_cocuklar = canli_cocuks + cansız_fakat_alt_soylu_cocuks


			temporary_mirası_paylasacak_kisi_sayısı = len(birlesmis_birinci_derece_mirasci_cocuklar)


			kisi_bası_dusen_pay = miras_para/temporary_mirası_paylasacak_kisi_sayısı

			temporary_result_1 = []

			for mirascı_birey in canli_cocuks:

				temp_val_1 = (mirascı_birey, kisi_bası_dusen_pay)

				temporary_result_1.append(temp_val_1)

			bos_lst = []	

			for mirascı_birey2 in cansız_fakat_alt_soylu_cocuks:

				bos_lst = bos_lst + partnere_para_vermeyen_pg1(mirascı_birey2, lst, kisi_bası_dusen_pay)

			result = bos_lst + temporary_result_1
			
			return result


def canlı_alt_soy_var_mi(olen_kisi, aile):

		if olen_kisi == []:

			return []
			
		else:	

			canlı_alt_soy = []

			for kisi in aile:

				if type(olen_kisi) == list:

					if kisi[0] == olen_kisi[0]:

						childeren = kisi[4]

						for child in childeren:

							for birey in aile:

								if birey[0] == child:

									if birey[-1] == "not dead":

										canlı_alt_soy.append(birey[0])

									elif birey[-1] == "DEPARTED":
									
										pass

						if childeren != []:				

							return(canlı_alt_soy + canlı_alt_soy_var_mi(childeren[1:],aile)+canlı_alt_soy_var_mi(olen_kisi[1:],aile))

						elif childeren == []:

							return(canlı_alt_soy+canlı_alt_soy_var_mi(olen_kisi[1:],aile))					

				elif type(olen_kisi) == str:	

					if kisi[0] == olen_kisi:

						childeren = kisi[4]

						for child in childeren:

							for birey in aile:

								if birey[0] == child:

									if birey[-1] == "not dead":

										canlı_alt_soy.append(birey[0])

									elif birey[-1] == "DEPARTED":
									
										pass

						if childeren != []:				

							return(canlı_alt_soy + canlı_alt_soy_var_mi(childeren[0],aile) + canlı_alt_soy_var_mi(childeren[1:],aile))

						elif childeren == []:

							return(canlı_alt_soy)					


def helper_aile_olusturucu(lst):

	x = []

	for data in lst:

		x.append(data.split())

	aile_olacak_list = []

	birilerinin_cocukları = []

	esi_var_olanlar = []


	for veri in x:

		if veri[0] == "CHILD":

			childs = veri[3:]

			for childeren in childs:

				aile_olacak_list.append([childeren, veri[1], veri[2]])

				birilerinin_cocukları.append(childeren)


	for data in x:

		if data[0] == "CHILD":

			anne = data[1] 
			
			baba = data[2]

			if anne not in birilerinin_cocukları and [anne, [], []] not in aile_olacak_list:

				aile_olacak_list.append([anne, [], []])

			if baba not in birilerinin_cocukları and [baba, [], []] not in aile_olacak_list:
				
				aile_olacak_list.append([baba, [], []])


	for veri in x: 

		if veri[0] == "MARRIED":

			kisi_1 = veri[1] 

			kisi_2 = veri[2]

			for insan in aile_olacak_list:

				if insan[0] == kisi_1:

					insan.append(kisi_2)

			for insan2 in aile_olacak_list:
				
				if insan2[0] == kisi_2:

					insan2.append(kisi_1)

	for veri in x:

		if veri[0] == "MARRIED":

			kisi_1 = veri[1] 

			kisi_2 = veri[2]

			isimler_listesi = []

			for human in aile_olacak_list:

				isimler_listesi.append(human[0])

			if [kisi_1, [], [], kisi_2] not in aile_olacak_list and kisi_1 not in isimler_listesi:

				aile_olacak_list.append([kisi_1, [], [], kisi_2])

			if [kisi_2, [] ,[], kisi_1] not in aile_olacak_list and kisi_2 not in isimler_listesi:
			
				aile_olacak_list.append([kisi_2,[] ,[] ,kisi_1])			


	for insancık in aile_olacak_list:

		if len(insancık) == 3:

			insancık.append([])

	for veri in x:

		if veri[0] == "CHILD":

			childs = veri[3:]

			anne = veri[1]

			baba = veri[2]

			for kisi in aile_olacak_list:

				if kisi[0] == anne:

					kisi.append(childs)

			for kisi2 in aile_olacak_list:		

				if kisi2[0] == baba:
				
					kisi2.append(childs)


	for insan in aile_olacak_list: 

		if len(insan) == 4:

			insan.append([])

		elif len(insan) == 5:

			pass 
		
		elif len(insan)	> 5:

			karısık_cocuklar = insan[4:]

			birlesik_cocuklar = []

			for bebe in karısık_cocuklar:

				birlesik_cocuklar.extend(bebe)

				insan[4:] = [birlesik_cocuklar]	


	for veri in x:

		if veri[0] == "DEPARTED":

			who_passed_away = veri[1]

			for person in aile_olacak_list:

				if person[0] == who_passed_away:

					person.append("DEPARTED")


	for veri in x:

		if veri[0] == "DECEASED":

			considered_death_person = veri[1]

			money = veri[2] 

			for insan in aile_olacak_list:

				if insan[0] == considered_death_person:

					if insan[-1] == "DEPARTED":

						insan[-1] =	"DECEASED"

						insan.append(money)

					else:
					
						insan.append("DECEASED")
						insan.append(money)

			aile_olacak_list_de_bulunan_current_isimler = []

			for pers in aile_olacak_list:

				aile_olacak_list_de_bulunan_current_isimler.append(pers[0])

			if considered_death_person in aile_olacak_list_de_bulunan_current_isimler:
			
				pass

			elif considered_death_person not in aile_olacak_list_de_bulunan_current_isimler:

				aile_olacak_list.append([considered_death_person, [], [], [], [],"DECEASED", money])


	for person in aile_olacak_list:

		if len(person) == 5:

			person.append("not dead")

		elif len(person) > 5:

			pass
			
	return(aile_olacak_list)

def inheritance_help(liste):

	aile = helper_aile_olusturucu(liste)

	for person in aile:

		if person[-2] == "DECEASED":

			# KOD BURAYA GELDİĞİ ZAMAN ARTIK MİRASÇININ ÜZERİNDE OLMUŞ OLUYORUZ, BU NOKTADAN SONRA ONUN ÜZERİNDE İŞLEMLER YAPILACAK

			mirascının_ismi = person[0]
			miras_para = float(person[-1])

			mirascının_annesi = person[1]	
			# mirascının_annesi = [] Bos list olabilir

			mirascının_babası = person[2]
			mirascının_partneri_lst = []
			mirascının_partneri = person[3]

			for aranan in aile:
				if aranan[0] == mirascının_partneri:
					mirascının_partneri_lst = aranan

			mirascının_annesi_lst = []
			mirascının_babası_lst = []

			mirascının_baba_tarafından_dedesi_lst = []
			mirascının_baba_tarafından_babaannesi_lst = []

			mirascının_anne_tarafından_dedesi_lst = []
			mirascının_anne_tarafından_anaannesi_lst = []

			for sahıs in aile:

				if sahıs[0] == mirascının_annesi:
					mirascının_annesi_lst.append(sahıs)

					mom = sahıs[1]
					dad = sahıs[2]

					for sahsiyet in aile:

						if sahsiyet[0] == mom:

							#burada anaanneyi bulduk artık

							mirascının_anne_tarafından_anaannesi_lst.append(sahsiyet)

						if sahsiyet[0] == dad:
						
							mirascının_anne_tarafından_dedesi_lst.append(sahsiyet)

				if sahıs[0] == mirascının_babası:

					mirascının_babası_lst.append(sahıs)

					mom_2 = sahıs[1]
					dad_2 = sahıs[2]

					for sahsi_kisilik in aile:

						if sahsi_kisilik[0] == mom_2:

							#burada anaanneyi bulduk artık

							mirascının_baba_tarafından_babaannesi_lst.append(sahsi_kisilik)

						if sahsi_kisilik[0] == dad_2:
						
							mirascının_baba_tarafından_dedesi_lst.append(sahsi_kisilik)

			# artık gradparent listelerden artık dede ve babaanneyi çekmek kaldı hemen aşağıda yapalım


			#---------------------------DİKKAT ET------------------------------


			birinci_dereceden_ust_soy = mirascının_annesi_lst + mirascının_babası_lst + mirascının_baba_tarafından_dedesi_lst + mirascının_baba_tarafından_babaannesi_lst +mirascının_anne_tarafından_dedesi_lst +mirascının_anne_tarafından_anaannesi_lst

			ust_soy_canlılık_bilgileri = []

			for item in birinci_dereceden_ust_soy:

				ust_soy_canlılık_bilgileri.append(item[-1])

			varsa_canlı_alt_soy_listesi = canlı_alt_soy_var_mi(mirascının_ismi, aile)

			#BURADAN İTİBAREN KODUMUZ CUNKU PG1 CAGIRMAKTA...

			if varsa_canlı_alt_soy_listesi == []:

				#PG2 YA DA PG3 OLACAK, ON CONSTRUCTİON

				if birinci_dereceden_ust_soy == []:

					# ust soy yok, yani bilgi yok ya da ust soy olu

					if "not dead" in mirascının_partneri_lst:

						return [(mirascının_partneri_lst[0], float(miras_para))]

					else: 

					#bu else durmunu handle etmemiz lazım # KİMSEYE PARANIN GİTMEDİĞİ DURUM
					
						return []	
				
				elif "not dead" not in ust_soy_canlılık_bilgileri:

					anne_ya_da_baba_alt_soy_var_mı = []

					olmus_annenin_alt_soyu_var_mı = canlı_alt_soy_var_mi(mirascının_annesi, aile)

					olmus_babanın_alt_soyu_var_mı = canlı_alt_soy_var_mi(mirascının_babası, aile)

					
					anne_ya_da_baba_alt_soy_var_mı += olmus_babanın_alt_soyu_var_mı

					anne_ya_da_baba_alt_soy_var_mı += olmus_annenin_alt_soyu_var_mı

					if anne_ya_da_baba_alt_soy_var_mı != []:

						#PG2 UYgulanacak

						#ANNE BABA HER İKİSİ DE ÖLÜ

						# EŞİNİN CANLILIĞINI KONTORL ETMEN LAZIM

						if mirascının_partneri_lst != []:

							if mirascının_partneri_lst[-1] == "not dead":

								anne_tarafından_alacaklılar = []

								baba_tarafından_alacaklılar = []
							
								if olmus_annenin_alt_soyu_var_mı != []:

									anne_tarafından_alacaklılar = olmus_annenin_alt_soyu_var_mı

								if olmus_babanın_alt_soyu_var_mı != []:

									baba_tarafından_alacaklılar = olmus_babanın_alt_soyu_var_mı

								if anne_tarafından_alacaklılar != [] and baba_tarafından_alacaklılar != []:
								
									buranın_sonucu = []

									buranın_sonucu += partnere_para_vermeyen_pg1(mirascının_annesi, aile, miras_para/4)

									buranın_sonucu += partnere_para_vermeyen_pg1(mirascının_babası, aile, miras_para/4)

									buranın_sonucu += [(mirascının_partneri, miras_para/2)]

									return buranın_sonucu			

								elif anne_tarafından_alacaklılar == [] and baba_tarafından_alacaklılar != []:

									buranın_sonucu = []

									buranın_sonucu += partnere_para_vermeyen_pg1(mirascının_babası, aile, miras_para/2)

									buranın_sonucu += [(mirascının_partneri, miras_para/2)]

									return buranın_sonucu

								elif anne_tarafından_alacaklılar != [] and baba_tarafından_alacaklılar == []:

									buranın_sonucu = []

									buranın_sonucu += partnere_para_vermeyen_pg1(mirascının_annesi, aile, miras_para/2)

									buranın_sonucu += [(mirascının_partneri, miras_para/2)]

									return buranın_sonucu
							
						if mirascının_partneri_lst == [] or mirascının_partneri_lst[-1] == "DEPARTED":

							anne_tarafından_alacaklılar = []

							baba_tarafından_alacaklılar = []
						
							if olmus_annenin_alt_soyu_var_mı != []:

								anne_tarafından_alacaklılar = olmus_annenin_alt_soyu_var_mı

							if olmus_babanın_alt_soyu_var_mı != []:

								baba_tarafından_alacaklılar = olmus_babanın_alt_soyu_var_mı

							if anne_tarafından_alacaklılar != [] and baba_tarafından_alacaklılar != []:
							
								buranın_sonucu = []

								buranın_sonucu += partnere_para_vermeyen_pg1(mirascının_annesi, aile, miras_para/2)

								buranın_sonucu += partnere_para_vermeyen_pg1(mirascının_babası, aile, miras_para/2)

								return buranın_sonucu			

							elif anne_tarafından_alacaklılar == [] and baba_tarafından_alacaklılar != []:

								buranın_sonucu = []

								buranın_sonucu += partnere_para_vermeyen_pg1(mirascının_babası, aile, miras_para)

								return buranın_sonucu

							elif anne_tarafından_alacaklılar != [] and baba_tarafından_alacaklılar == []:

								buranın_sonucu = []

								buranın_sonucu += partnere_para_vermeyen_pg1(mirascının_annesi, aile, miras_para)

								return buranın_sonucu

					elif anne_ya_da_baba_alt_soy_var_mı == []:
	
						#PG3 uygulanacak	 
				
						birlestirilmis_grand_parents = mirascının_baba_tarafından_dedesi_lst + mirascının_baba_tarafından_babaannesi_lst + mirascının_anne_tarafından_dedesi_lst +mirascının_anne_tarafından_anaannesi_lst

						partner_hayatta_mı = []

						for insan in aile:

							if insan[0] == mirascının_partneri:

								if "not dead" in insan:

									partner_hayatta_mı.append(insan[0])

								elif "DEPARTED" in insan:

									pass

						if partner_hayatta_mı != []:
						
							#partner hayattadır

							partner_hayatta_mı[0] = (mirascının_partneri, miras_para*(3/4))

							miras_para = (1/4)*miras_para

						elif partner_hayatta_mı == []:
						
							pass

						canlı_grandparents = []
						
						cansız_fakat_alt_soylu_grandparents = []

						for grandp in birlestirilmis_grand_parents:

							if "not dead" in grandp:

								canlı_grandparents.append(grandp[0]) 

								#grandp yi mi yoksa grandp[0] yu mu koysam emin değilim buraya dikkat 

							elif "DEPARTED" in grandp:
							
								varsa_grandparentın_canlı_alt_soy_listesi = canlı_alt_soy_var_mi(grandp[0], aile)

								if varsa_grandparentın_canlı_alt_soy_listesi != []:

									cansız_fakat_alt_soylu_grandparents.append(grandp[0])

								elif varsa_grandparentın_canlı_alt_soy_listesi == []:
								
									pass

						if cansız_fakat_alt_soylu_grandparents != []:			

							birlesmis_mirasci_granparents = canlı_grandparents + cansız_fakat_alt_soylu_grandparents

							granparentsda_temporary_mirası_paylasacak_kisi_sayısı = len(birlesmis_mirasci_granparents)

							granparents_ıcın_kisi_bası_dusen_pay = miras_para/granparentsda_temporary_mirası_paylasacak_kisi_sayısı

							temporary_result_grandp = []

							for miras_adayı in canlı_grandparents:

								temp_val = (miras_adayı, granparents_ıcın_kisi_bası_dusen_pay)

								temporary_result_grandp.append(temp_val)

							empty_lst = []
							
							for olmus_miras_adayı in cansız_fakat_alt_soylu_grandparents:

								empty_lst = empty_lst + partnere_para_vermeyen_pg1(olmus_miras_adayı, aile, granparents_ıcın_kisi_bası_dusen_pay)

							burda_result = empty_lst + temporary_result_grandp

							if partner_hayatta_mı != []:

								artık_son_result = partner_hayatta_mı + burda_result

								return artık_son_result

							elif partner_hayatta_mı == []:
							
								return burda_result

						elif cansız_fakat_alt_soylu_grandparents == []:

							if "not dead" in mirascının_partneri_lst:

								return [(mirascının_partneri_lst[0], float(miras_para))]

							else: 

								return []								
				
				else:

					anne_baba_birlesmis_lst = mirascının_annesi_lst + mirascının_babası_lst

					anne_baba_canlılıgı = []

					for birey in anne_baba_birlesmis_lst:

						if birey == []:

							pass

						elif birey != []:
						
							anne_baba_canlılıgı.append(birey[-1])

					if "not dead" in anne_baba_canlılıgı:

						# anne ve babaya PG2 uygulamamız lazım...

						mommy = anne_baba_birlesmis_lst[0] # bunlar su an liste

						daddy = anne_baba_birlesmis_lst[1]


						if mommy[-1] == "not dead" and daddy[-1] == "not dead":

							#her ikisi de ölü değilse

							if mirascının_partneri_lst != []:  

								if mirascının_partneri_lst[-1] == "not dead":

									return[(mirascının_partneri_lst[0], miras_para/2),(mommy[0], miras_para/4), (daddy[0], miras_para/4)]

							if mirascının_partneri_lst == [] or mirascının_partneri_lst[-1] == "DEPARTED":

								return [(mommy[0],miras_para/2),(daddy[0],miras_para/2)]

						elif mommy[-1] == "DEPARTED" and daddy[-1] == "not dead":

							#anne olu baba yasıyorsa

							varsa_anne_canlı_alt_soy_listesi = canlı_alt_soy_var_mi(mommy[0], aile)

							if varsa_anne_canlı_alt_soy_listesi != []:

								if mirascının_partneri_lst != []:  

									if mirascının_partneri_lst[-1] == "not dead":

										anne_altındaki_paydaslar_ve_alacakları = partnere_para_vermeyen_pg1(mommy[0], aile, miras_para/4)

										sonuc_of_here = [(daddy[0], miras_para/4)] + [(mirascının_partneri_lst[0], miras_para/2)] + anne_altındaki_paydaslar_ve_alacakları

										return sonuc_of_here

								if mirascının_partneri_lst == [] or mirascının_partneri_lst[-1] == "DEPARTED":

									anne_altındaki_paydaslar_ve_alacakları = partnere_para_vermeyen_pg1(mommy[0], aile, miras_para/2)

									sonuc_of_here = [(daddy[0], miras_para/2)] + anne_altındaki_paydaslar_ve_alacakları

									return sonuc_of_here


							elif varsa_anne_canlı_alt_soy_listesi == []:

								if mirascının_partneri_lst != []:  

									if mirascının_partneri_lst[-1] == "not dead":
							
										return[(mirascının_partneri_lst[0], miras_para/2),(daddy[0], miras_para/2)]

								if mirascının_partneri_lst == [] or mirascının_partneri_lst[-1] == "DEPARTED":
								
									return[(daddy[0], miras_para)]	 	


						elif mommy[-1] == "not dead" and daddy[-1] == "DEPARTED":
							
							#baba ölü anne yaşıyorsa

							varsa_baba_canlı_alt_soy_listesi = canlı_alt_soy_var_mi(daddy[0], aile)

							if varsa_baba_canlı_alt_soy_listesi != []:

								if mirascının_partneri_lst != []:

									if mirascının_partneri_lst[-1] == "not dead":

										baba_altındaki_paydaslar_ve_alacakları = partnere_para_vermeyen_pg1(daddy[0], aile, miras_para/4)

										sonuc_of_here = [(mommy[0],miras_para/4)] + [(mirascının_partneri_lst[0], miras_para/2)] + baba_altındaki_paydaslar_ve_alacakları

										return sonuc_of_here

								if mirascının_partneri_lst == [] or mirascının_partneri_lst[-1] == "DEPARTED":

									baba_altındaki_paydaslar_ve_alacakları = partnere_para_vermeyen_pg1(daddy[0], aile, miras_para/2)

									sonuc_of_here = [(mommy[0],miras_para/2)] + baba_altındaki_paydaslar_ve_alacakları

									return sonuc_of_here


							elif varsa_baba_canlı_alt_soy_listesi == []:

								if mirascının_partneri_lst != []:

									if mirascının_partneri_lst[-1] == "not dead": 

										return[(mirascının_partneri_lst[0], miras_para/2),(mommy[0], miras_para/2)]

								if mirascının_partneri_lst == [] or mirascının_partneri_lst[-1] == "DEPARTED":	

									return[(mommy[0], miras_para)]



					elif "not dead" not in anne_baba_canlılıgı:

						anne_ya_da_baba_alt_soy_var_mı = []

						olmus_annenin_alt_soyu_var_mı = canlı_alt_soy_var_mi(mirascının_annesi, aile)

						olmus_babanın_alt_soyu_var_mı = canlı_alt_soy_var_mi(mirascının_babası, aile)

						anne_ya_da_baba_alt_soy_var_mı += olmus_babanın_alt_soyu_var_mı

						anne_ya_da_baba_alt_soy_var_mı += olmus_annenin_alt_soyu_var_mı

						if anne_ya_da_baba_alt_soy_var_mı != []:

							#PG2 UYgulanacak

							if mirascının_partneri_lst != []:

								if mirascının_partneri_lst[-1] == "not dead":

									anne_tarafından_alacaklılar = []

									baba_tarafından_alacaklılar = []
								
									if olmus_annenin_alt_soyu_var_mı != []:

										anne_tarafından_alacaklılar = olmus_annenin_alt_soyu_var_mı

									if olmus_babanın_alt_soyu_var_mı != []:

										baba_tarafından_alacaklılar = olmus_babanın_alt_soyu_var_mı

									if anne_tarafından_alacaklılar != [] and baba_tarafından_alacaklılar != []:
									
										buranın_sonucu = []

										buranın_sonucu += partnere_para_vermeyen_pg1(mirascının_annesi, aile, miras_para/4)

										buranın_sonucu += partnere_para_vermeyen_pg1(mirascının_babası, aile, miras_para/4)

										buranın_sonucu += [(mirascının_partneri, miras_para/2)]

										return buranın_sonucu			

									elif anne_tarafından_alacaklılar == [] and baba_tarafından_alacaklılar != []:

										buranın_sonucu = []

										buranın_sonucu += partnere_para_vermeyen_pg1(mirascının_babası, aile, miras_para/2)

										buranın_sonucu += [(mirascının_partneri, miras_para/2)]

										return buranın_sonucu

									elif anne_tarafından_alacaklılar != [] and baba_tarafından_alacaklılar == []:

										buranın_sonucu = []

										buranın_sonucu += partnere_para_vermeyen_pg1(mirascının_annesi, aile, miras_para/2)

										buranın_sonucu += [(mirascının_partneri, miras_para/2)]

										return buranın_sonucu
								
							if mirascının_partneri_lst == [] or mirascının_partneri_lst[-1] == "DEPARTED":

								anne_tarafından_alacaklılar = []

								baba_tarafından_alacaklılar = []
							
								if olmus_annenin_alt_soyu_var_mı != []:

									anne_tarafından_alacaklılar = olmus_annenin_alt_soyu_var_mı

								if olmus_babanın_alt_soyu_var_mı != []:

									baba_tarafından_alacaklılar = olmus_babanın_alt_soyu_var_mı

								if anne_tarafından_alacaklılar != [] and baba_tarafından_alacaklılar != []:
								
									buranın_sonucu = []

									buranın_sonucu += partnere_para_vermeyen_pg1(mirascının_annesi, aile, miras_para/2)

									buranın_sonucu += partnere_para_vermeyen_pg1(mirascının_babası, aile, miras_para/2)

									return buranın_sonucu			

								elif anne_tarafından_alacaklılar == [] and baba_tarafından_alacaklılar != []:

									buranın_sonucu = []

									buranın_sonucu += partnere_para_vermeyen_pg1(mirascının_babası, aile, miras_para)

									return buranın_sonucu

								elif anne_tarafından_alacaklılar != [] and baba_tarafından_alacaklılar == []:

									buranın_sonucu = []

									buranın_sonucu += partnere_para_vermeyen_pg1(mirascının_annesi, aile, miras_para)

									return buranın_sonucu	


						elif anne_ya_da_baba_alt_soy_var_mı == []:
							
							#PG3 uygulanacak	 

							birlestirilmis_grand_parents = mirascının_baba_tarafından_dedesi_lst + mirascının_baba_tarafından_babaannesi_lst + mirascının_anne_tarafından_dedesi_lst +mirascının_anne_tarafından_anaannesi_lst

							partner_hayatta_mı = []

							for insan in aile:

								if insan[0] == mirascının_partneri:

									if "not dead" in insan:

										partner_hayatta_mı.append(insan[0])

									elif "DEPARTED" in insan:

										pass

							if partner_hayatta_mı != []:
							
								#partner hayattadır

								partner_hayatta_mı[0] = (mirascının_partneri, miras_para*(3/4))

								miras_para = (1/4)*miras_para

							elif partner_hayatta_mı == []:
							
								pass

							canlı_grandparents = []
							
							cansız_fakat_alt_soylu_grandparents = []

							for grandp in birlestirilmis_grand_parents:

								if "not dead" in grandp:

									canlı_grandparents.append(grandp[0]) #grandp yi mi yoksa grandp[0] yu mu koysam emin değilim buraya çok dikkat 

								elif "DEPARTED" in grandp:
								
									varsa_grandparentın_canlı_alt_soy_listesi = canlı_alt_soy_var_mi(grandp[0], aile)

									if varsa_grandparentın_canlı_alt_soy_listesi != []:

										cansız_fakat_alt_soylu_grandparents.append(grandp[0])

									elif varsa_grandparentın_canlı_alt_soy_listesi == []:
									
										pass

							birlesmis_mirasci_granparents = canlı_grandparents + cansız_fakat_alt_soylu_grandparents

							granparentsda_temporary_mirası_paylasacak_kisi_sayısı = len(birlesmis_mirasci_granparents)

							granparents_ıcın_kisi_bası_dusen_pay = miras_para/granparentsda_temporary_mirası_paylasacak_kisi_sayısı

							temporary_result_grandp = []

							for miras_adayı in canlı_grandparents:

								temp_val = (miras_adayı, granparents_ıcın_kisi_bası_dusen_pay)

								temporary_result_grandp.append(temp_val)

							empty_lst = []
							
							for olmus_miras_adayı in cansız_fakat_alt_soylu_grandparents:

								empty_lst = empty_lst + partnere_para_vermeyen_pg1(olmus_miras_adayı, aile, granparents_ıcın_kisi_bası_dusen_pay)

							burda_result = empty_lst + temporary_result_grandp

							if partner_hayatta_mı != []:

								artık_son_result = partner_hayatta_mı + burda_result

								return artık_son_result

							elif partner_hayatta_mı == []:
							
								return burda_result

			elif varsa_canlı_alt_soy_listesi != []:

				sonuc = pg1(person[0], aile, miras_para)

				return sonuc

