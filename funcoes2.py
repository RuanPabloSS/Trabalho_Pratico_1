def loginUsuario(perfil):

    if (str.lower(perfil) == 'admin'):

        print('Bem-vindo, Administrador')
    
    else:

        print('Bem-vindo, Usuário')

loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')
loginUsuario('aDMIN')
loginUsuario('ADMIN')