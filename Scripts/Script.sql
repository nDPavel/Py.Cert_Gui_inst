select link.IdCert,
  link.idPodr,
  u.id,
  u.Name,
  us.id,
  us.Name,
  cd.DateCre,
  cd.DateExp,
  cd.PodrName,
  cd.UserName
         from Unit as U,
              UnitSubject as us,
              CertDate as cd,
              LinkCertORUnitSub as link
                      WHERE 1=1
                        and link.idPodr = us.id
                        and link.IdCert = cd.id
                        and U.id = us.idPodr
                        and us.Name = 'Alapaevsk'

                        
                        select * from Unit 

